import os
import subprocess
import re

def get_original_description(file_path):
    try:
        # Get content from origin/main
        result = subprocess.run(['git', 'show', f'origin/main:{file_path}'], capture_output=True, text=True)
        if result.returncode != 0:
            return None
        content = result.stdout
        # Extract frontmatter description
        match = re.search(r'^description: (.*?)^---', content, re.DOTALL | re.MULTILINE)
        if match:
            return match.group(1).strip()
    except Exception as e:
        print(f"Error getting original description for {file_path}: {e}")
    return None

def process_file(file_path):
    print(f"Processing {file_path}...")
    with open(file_path, 'r') as f:
        lines = f.readlines()

    new_lines = []
    in_frontmatter = False
    frontmatter_indices = []
    
    # Identify frontmatter
    for i, line in enumerate(lines):
        if line.strip() == '---':
            frontmatter_indices.append(i)
            if len(frontmatter_indices) == 2:
                break
    
    if len(frontmatter_indices) == 2:
        # Restore description from main
        # We need to find the relative path from repo root
        repo_root = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
        rel_path = os.path.relpath(file_path, repo_root)
        
        orig_content = subprocess.run(['git', 'show', f'origin/main:{rel_path}'], capture_output=True, text=True).stdout
        if orig_content:
            orig_desc_match = re.search(r'^description: (.*?)\n(?=---|\w+:)', orig_content, re.DOTALL | re.MULTILINE)
            if not orig_desc_match:
                # Try with block style
                orig_desc_match = re.search(r'^description: ([>|].*?)\n(?=---|\w+:)', orig_content, re.DOTALL | re.MULTILINE)
            
            if orig_desc_match:
                orig_desc = orig_desc_match.group(0).strip()
                # Replace current description in frontmatter
                start, end = frontmatter_indices
                frontmatter = lines[start:end+1]
                new_frontmatter = []
                desc_replaced = False
                for fline in frontmatter:
                    if fline.startswith('description:'):
                        if not desc_replaced:
                            new_frontmatter.append(orig_desc + '\n')
                            desc_replaced = True
                    elif desc_replaced and (fline.startswith('  ') or fline.strip() == ''):
                        # Skip continued lines of old description
                        continue
                    else:
                        new_frontmatter.append(fline)
                
                # If description was multiline in orig but single line now, we replaced it.
                # If it was not found, keep as is.
                if desc_replaced:
                    new_lines.extend(new_lines_from_body := []) # placeholder
                    # We'll re-assemble later
                else:
                    new_frontmatter = frontmatter
            else:
                new_frontmatter = lines[frontmatter_indices[0]:frontmatter_indices[1]+1]
        else:
            new_frontmatter = lines[frontmatter_indices[0]:frontmatter_indices[1]+1]
    else:
        new_frontmatter = []

    # Process body
    body_start = frontmatter_indices[1] + 1 if len(frontmatter_indices) == 2 else 0
    body_lines = lines[body_start:]
    
    processed_body = []
    in_code_block = False
    for line in body_lines:
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            processed_body.append(line)
            continue
        
        if not in_code_block:
            # Fix 'You MUST' sentences
            # Look for '. You MUST' or '; You MUST' or even 'Sentence. You MUST'
            # But avoid matching if it's already at the start of a line
            if 'You MUST' in line and not line.strip().startswith('You MUST') and not line.strip().startswith('- You MUST'):
                # Split at the sentence boundary before You MUST
                # Use a simple regex to find ". You MUST" or similar
                new_line = re.sub(r'([\.!;])\s+(You MUST)', r'\1\n\2', line)
                processed_body.extend(new_line.splitlines(keepends=True))
            else:
                processed_body.append(line)
        else:
            processed_body.append(line)

    # Special case for agentskills/SKILL.md
    if 'agentskills/SKILL.md' in file_path:
        # Move misplaced line
        misplaced_line = "The Agent Skills open standard provides a framework for structuring and specifying skills to ensure portability across different AI systems and agent hosts. Agent Skills work with GitHub Copilot (Cloud, CLI, and VS Code), Claude Code, OpenCode, and other compliant agents. Agent Skills are self-contained folders with instructions and bundled resources that teach AI agents specialized capabilities, unlike custom instructions which only define coding standards."
        
        # Remove from body
        final_body = []
        found_misplaced = False
        for line in processed_body:
            if misplaced_line in line:
                found_misplaced = True
                continue
            final_body.append(line)
        
        # Insert after main header (# Agent Skills (Standard))
        header_index = -1
        for i, line in enumerate(final_body):
            if line.strip() == '# Agent Skills (Standard)':
                header_index = i
                break
        
        if header_index != -1:
            # Insert after header and possibly after the markdownlint disable comment
            insert_pos = header_index + 1
            if insert_pos < len(final_body) and 'markdownlint-disable' in final_body[insert_pos]:
                insert_pos += 1
            
            # Ensure there are newlines
            final_body.insert(insert_pos, '\n' + misplaced_line + '\n')
        processed_body = final_body

    final_content = lines[:frontmatter_indices[0]] + new_frontmatter + processed_body
    
    with open(file_path, 'w') as f:
        f.writelines(final_content)

def main():
    repo_root = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
    for root, dirs, files in os.walk(repo_root):
        if '.git' in dirs:
            dirs.remove('.git')
        for file in files:
            if file == 'SKILL.md':
                process_file(os.path.join(root, file))

if __name__ == "__main__":
    main()
