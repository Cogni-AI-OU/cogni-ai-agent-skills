---
name: unicode
description: 'Reference for Unicode character hex ranges and regex blocks for searching, matching, or filtering text across international scripts and symbols.'
---

# Unicode Regex Ranges

<!-- markdownlint-disable MD013 MD023 MD031 MD032 MD033 -->

## When to Use This Skill

- You need to search, match, or filter text containing specific Unicode ranges (e.g., CJK, Cyrillic, Emoji).
- You are writing regex to validate or extract international characters, symbols, or specific scripts.
- You need a reference for exact hexadecimal ranges for various languages or symbols.

## Core Process

When tasked with matching specific languages or symbols:
1. Identify the target script, language, or symbol category.
2. Look up the precise hex range (`\x{XXXX}-\x{YYYY}`) in the reference tables below.
3. Insert the range into your tool's regex syntax (e.g., `[\x{0100}-\x{024F}]+` for PCRE-compliant engines like `rg` or `grep -P`).

## Core Principles

- **Engine Compatibility**: The ranges provided use `\x{XXXX}` syntax, which is standard in PCRE (e.g., ripgrep, PHP, Python via `regex` module). In other languages like JavaScript or standard Python, you may need `\uXXXX` or `\U000XXXXX` for surrogate pairs.
- **Combined Ranges**: Multiple ranges can be grouped in character classes: `[\x{0900}-\x{097F}\x{0A00}-\x{0A7F}]`.
- **Case Sensitivity**: For ranges containing cased letters, ensure your tool is set to case-insensitive mode if required, though ranges often cover both.

## Unicode Range Reference

### East Asian Scripts

| Script / Description | PCRE Regex Range |
| --- | --- |
| Chinese (Basic) | `[\x{4E00}-\x{9FFF}]` |
| CJK Extension A | `[\x{3400}-\x{4DBF}]` |
| CJK Extension B | `[\x{20000}-\x{2A6DF}]` |
| Halfwidth Katakana | `[\x{FF66}-\x{FF9F}]` |
| Hiragana & Katakana | `[\x{3040}-\x{309F}\x{30A0}-\x{30FF}]` |
| Hangul Jamo (Basic) | `[\x{1100}-\x{11FF}]` |
| Hangul Compat Jamo | `[\x{3130}-\x{318F}]` |
| Hangul Syllables | `[\x{AC00}-\x{D7AF}]` |
| Hangul Jamo Ext-A | `[\x{A960}-\x{A97F}]` |
| All Korean Ranges | `[\x{1100}-\x{11FF}\x{3130}-\x{318F}\x{AC00}-\x{D7AF}\x{A960}-\x{A97F}]` |
| All CJK Combined | `[\x{4E00}-\x{9FFF}\x{3400}-\x{4DBF}\x{20000}-\x{2A6DF}]` |
| CJK Radicals Supp | `[\x{2E80}-\x{2EFF}]` |
| CJK Strokes | `[\x{31C0}-\x{31EF}]` |
| CJK Symbols | `[\x{3000}-\x{303F}\x{3200}-\x{32FF}]` |
| CJK Compatibility | `[\x{3300}-\x{33FF}]` |
| CJK Extension C | `[\x{2A700}-\x{2B73F}]` |
| CJK Extension D | `[\x{2B740}-\x{2B81F}]` |

### South Asian Scripts

| Script / Description | PCRE Regex Range |
| --- | --- |
| Bengali | `[\x{0980}-\x{09FF}]` |
| Devanagari (Hindi) | `[\x{0900}-\x{097F}]` |
| Gujarati | `[\x{0A80}-\x{0AFF}]` |
| Gurmukhi (Punjabi) | `[\x{0A00}-\x{0A7F}]` |
| Kannada | `[\x{0C80}-\x{0CFF}]` |
| Malayalam | `[\x{0D00}-\x{0D7F}]` |
| Tamil | `[\x{0B80}-\x{0BFF}]` |
| Telugu | `[\x{0C00}-\x{0C7F}]` |
| Sinhala | `[\x{0D80}-\x{0DFF}]` |
| Oriya/Odia | `[\x{0B00}-\x{0B7F}]` |
| All Indic Scripts | `[\x{0900}-\x{0DFF}]` |

### Middle Eastern & African Scripts

| Script / Description | PCRE Regex Range |
| --- | --- |
| Arabic | `[\x{0621}-\x{0669}]` |
| Hebrew | `[\x{0590}-\x{05FE}]` |
| Ethiopic | `[\x{1200}-\x{137F}]` |
| N'Ko | `[\x{07C0}-\x{07FF}]` |
| Tifinagh | `[\x{2D30}-\x{2D7F}]` |
| Bamum | `[\x{A6A0}-\x{A6FF}]` |
| Adlam | `[\x{1E900}-\x{1E95F}]` |
| Syriac | `[\x{0700}-\x{074F}]` |
| Thaana | `[\x{0780}-\x{07BF}]` |

### European & Caucasian Scripts

| Script / Description | PCRE Regex Range |
| --- | --- |
| Armenian | `[\x{0531}-\x{0587}]` |
| Georgian | `[\x{10A0}-\x{10FF}]` |
| Greek | `[\x{0374}-\x{03FF}]` |
| Russian/Cyrillic | `[а-яёА-ЯЁ]` |
| Extended Cyrillic | `[\x{0400}-\x{04FF}\x{0500}-\x{052F}]` |
| Latin Accented Chars | `[ąęáàâäãåćéèêëńíìîïóòôöõúùûüçñýÿźż]` |
| Basic Latin | `[\x{0000}-\x{007F}]` |
| Latin-1 Supplement | `[\x{0080}-\x{00FF}]` |
| Latin Extended-A | `[\x{0100}-\x{017F}]` |
| Latin Extended-B | `[\x{0180}-\x{024F}]` |
| Latin Extended Add | `[\x{1E00}-\x{1EFF}]` |
| Gothic | `[\x{10330}-\x{1034F}]` |
| Runic | `[\x{16A0}-\x{16FF}]` |
| Ogham | `[\x{1680}-\x{169F}]` |
| Old Italic | `[\x{10300}-\x{1032F}]` |
| Glagolitic | `[\x{2C00}-\x{2C5F}]` |

### Southeast Asian & Other Scripts

| Script / Description | PCRE Regex Range |
| --- | --- |
| Khmer | `[\x{1780}-\x{17FF}]` |
| Lao | `[\x{0E80}-\x{0EFF}]` |
| Myanmar (Burmese) | `[\x{1000}-\x{109F}]` |
| Thai | `[\x{0E00}-\x{0E7F}]` |
| Mongolian | `[\x{1800}-\x{18AF}\x{11660}-\x{1167F}]` |
| Tibetan | `[\x{0F00}-\x{0FFF}]` |
| Balinese | `[\x{1B00}-\x{1B7F}]` |
| Javanese | `[\x{A980}-\x{A9DF}]` |
| Sundanese | `[\x{1B80}-\x{1BBF}]` |
| Yi Syllables | `[\x{A000}-\x{A48F}]` |

### Ancient Scripts

| Script / Description | PCRE Regex Range |
| --- | --- |
| Cuneiform | `[\x{12000}-\x{123FF}]` |
| Linear B | `[\x{10000}-\x{1007F}]` |
| Phoenician | `[\x{10900}-\x{1091F}]` |
| Egyptian Hieroglyphs | `[\x{13000}-\x{1342F}]` |
| Ancient Greek Numbers | `[\x{10140}-\x{1018F}]` |

### Symbols, Emojis, & Punctuation

| Category | PCRE Regex Range |
| --- | --- |
| General Punctuation | `[\x{2000}-\x{206F}]` |
| Emoji (All) | `[\x{1F300}-\x{1F9FF}]` |
| Emoji (Basic/Faces) | `[\x{1F1FF}-\x{1F64F}]` |
| Emoji (Transport) | `[\x{1F680}-\x{1F6FF}]` |
| Emoji (Food) | `[\x{1F32D}-\x{1F37F}]` |
| Arrows | `[\x{2190}-\x{21FF}\x{27F0}-\x{27FF}]` |
| Box Drawing / Shapes | `[\x{2500}-\x{25FF}]` |
| Currency Symbols | `[\x{20A0}-\x{20CF}]` |
| Dingbats | `[\x{2700}-\x{27BF}]` |
| Math Operators | `[\x{2200}-\x{22FF}\x{27C0}-\x{27EF}]` |
| Superscript/Subscript | `[\x{2070}-\x{209F}]` |
| Music Symbols | `[\x{1D100}-\x{1D1FF}\x{1D200}-\x{1D24F}]` |
| Braille Patterns | `[\x{2800}-\x{28FF}]` |
| Playing Cards | `[\x{1F0A0}-\x{1F0FF}]` |
| Chess Symbols | `[\x{2654}-\x{265F}]` |
| Dice & Dominoes | `[\x{2680}-\x{2685}\x{1F030}-\x{1F093}]` |
| Mahjong Tiles | `[\x{1F000}-\x{1F02F}]` |

### Phonetic & IPA

| Category | PCRE Regex Range |
| --- | --- |
| IPA Extensions | `[\x{0250}-\x{02AF}]` |
| Phonetic Extensions | `[\x{1D00}-\x{1D7F}\x{1D80}-\x{1DBF}]` |

## Gotchas

- **Surrogate Pairs in JS/Python**: If using standard JavaScript or Python (`re` module, not `regex`), you cannot use `\x{10000}`. You must either use the `\uXXXX` equivalent, `\U00010000`, or the ES6 `\u{10000}` syntax with the `/u` flag in JS.
- **Combined Ranges**: Take care not to overlap or create invalid ranges when combining (e.g., `[\x{2500}-\x{257F}\x{2580}-\x{259F}]` can safely be written as `[\x{2500}-\x{259F}]`).
- **Missing Characters**: The ranges cover primary codepoints but might omit rarely used characters placed in Extended blocks unless the Extended blocks are explicitly included.
