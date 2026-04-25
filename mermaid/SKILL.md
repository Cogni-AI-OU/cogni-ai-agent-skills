<!-- markdownlint-disable MD003 MD022 MD026 MD041 -->
---
name: mermaid
description: >-
  Guide for creating and maintaining Mermaid.js diagrams for documentation, architecture, and flow visualization.

  Maintained at: <https://github.com/Cogni-AI-OU/cogni-ai-agent-skills>

---
# Mermaid Skill

Expert in creating, optimizing, and troubleshooting Mermaid.js diagrams.
Prioritize clarity, readability, and adherence to Mermaid syntax standards for
various diagram types (flowcharts, sequence diagrams, Gantt charts, etc.).

## When to Activate

- User wants to visualize a process, architecture, or sequence of events using diagrams.
- User needs to update existing Mermaid diagrams in Markdown files.
- Agent needs to explain complex logic or flows using a visual representation.
- Troubleshooting syntax errors in existing Mermaid code blocks.

## Core Principles

- **Clarity First**: Diagrams should be easy to follow and not overly cluttered.
- **Consistent Styling**: Use consistent naming conventions and styling for nodes and edges.
- **Standard Syntax**: Adhere strictly to Mermaid.js syntax to ensure compatibility across viewers (GitHub, VS Code, etc.).
- **Minimalism**: Only include essential information in diagrams to maintain focus.

## Diagram Types & Patterns

### C4 Diagrams

The C4 model is a lean graphical notation technique for modeling the
architecture of software systems at different levels of abstraction.

- Use `C4Context`, `C4Container`, `C4Component`, or `C4Dynamic` to
  initialize the appropriate diagram level.
- Define an optional `title` to specify the diagram's purpose.
- Use entity definitions like `Person`, `System`, `System_Ext`,
  `Container`, and `Component` with the format
  `Type(alias, "Label", "Optional Description")`.
- Structure the layout using boundaries such as
  `Enterprise_Boundary(alias, "Label") { ... }`.
- Connect entities using `Rel(from, to, "Label", "Optional Tech")`.

Example demonstrating a System Context Diagram:

```mermaid
C4Context
    title System Context Diagram
    Person(customer, "Customer", "A customer of the bank.")
    Enterprise_Boundary(b0, "BankBoundary") {
        System(banking_system, "Banking System", "Allows customers to view accounts and make payments.")
        System_Ext(mail_system, "E-mail System", "The internal e-mail system.")
    }
    Rel(customer, banking_system, "Uses")
    Rel(banking_system, mail_system, "Sends e-mails using", "SMTP")
```

Docs: <https://mermaid.js.org/syntax/c4.html>

### Class Diagrams

A Class diagram is a static structure diagram that describes the
structure of a system by detailing its classes, attributes,
operations (or methods), and the relationships among objects.

- Use `classDiagram` to model object-oriented structures, including classes, interfaces, and their relationships.
- Define class members with visibility modifiers (`+` public, `-` private, `#` protected, `~` package/internal).
- Use relationships like inheritance (`<|--`), composition (`*--`), aggregation (`o--`), and dependency (`<..`).
- Include multiplicity (e.g., `"1"` to `"*"`) and annotations (e.g., `<<interface>>`, `<<abstract>>`) for detailed modeling.

Example with Relationships and Multiplicity:

```mermaid
classDiagram
    class Customer {
        +int id
        +String name
        +placeOrder()
    }
    class Order {
        -int orderId
        -Date date
        +calculateTotal() float
    }
    class Payment {
        <<interface>>
        +processPayment() bool
    }

    Customer "1" --> "*" Order : places
    Order "*" *-- "1..*" OrderItem : contains
    Order ..> Payment : depends on
```

Example with Generic Types, Abstract Classes, and Visibility:

```mermaid
classDiagram
    class Shape {
        <<abstract>>
        #String color
        +draw()*
        +getColor() String
    }
    class Circle {
        -double radius
        +draw()
    }
    class Collection~T~ {
        +add(item)
        +get(int index)
    }

    Shape <|-- Circle : Inheritance
    Collection~Shape~ o-- Shape : Aggregation
```

Docs: <https://mermaid.js.org/syntax/classDiagram.html>

### Entity Relationship Diagrams

An Entity-Relationship (ER) model describes interrelated things of
interest in a specific domain of knowledge. They specify relationships
that can exist between entity types and instances.

- Use `erDiagram` to model database schemas and entity relations.
- Define relationships using cardinality markers like `||--o{`
  (one-to-zero-or-more), `}o--|{` (zero-or-more to one-or-more), etc.
- Specify entity attributes alongside their data types inside blocks (`{ ... }`).
- Indicate Primary Keys (`PK`), Foreign Keys (`FK`), and Unique constraints (`UK`).

Example with Keys and Relationships:

```mermaid
erDiagram
    CUSTOMER ||--o{ ORDER : places
    ORDER ||--|{ ORDER_ITEM : contains
    PRODUCT ||--o{ ORDER_ITEM : includes

    CUSTOMER {
        int id PK
        string name
        string email UK
    }
    ORDER {
        int id PK
        int customer_id FK
        date orderDate
        string status
    }
    PRODUCT {
        int id PK
        string name
        float price
    }
    ORDER_ITEM {
        int order_id PK, FK
        int product_id PK, FK
        int quantity
        float price
    }
```

Docs: <https://mermaid.js.org/syntax/entityRelationshipDiagram.html>

### Flowcharts

- Use `flowchart` to show process flows, algorithms, or any step-by-step logic.
- Specify direction (e.g., `TD` for top-down, `LR` for left-right).
- Utilize different node shapes (e.g., `[rect]`, `(rounded)`, `{diamond}`, `[(database)]`).
- Group nodes logically using `subgraph` blocks.

Example with Subgraphs and Styling:

```mermaid
flowchart LR
    subgraph Client
        UI([User Interface])
    end

    subgraph Server
        API(API Gateway)
        Auth{Authorized?}
        App[Application Logic]
        DB[(Database)]
    end

    UI -- "REST Request" --> API
    API --> Auth
    Auth -- "Yes" --> App
    Auth -.->|"No (401 Unauthorized)"| UI
    App ==> DB

    classDef success fill:#d4edda,stroke:#28a745,stroke-width:2px;
    class DB success
```

Example Flowchart with New Shapes:

```mermaid
flowchart RL
    A@{ shape: manual-file, label: "File Handling"}
    B@{ shape: manual-input, label: "User Input"}
    C@{ shape: docs, label: "Multiple Documents"}
    D@{ shape: procs, label: "Process Automation"}
    E@{ shape: paper-tape, label: "Paper Records"}
```

Docs: <https://mermaid.js.org/syntax/flowchart.html>

### Gantt Charts

A Gantt chart is a type of bar chart that illustrates a project
schedule and the amount of time it takes for tasks to finish.

- Use `gantt` for creating project schedules and timelines.
- Define the `dateFormat` to specify how dates are parsed (e.g. `YYYY-MM-DD`).
- Divide tasks into categories using `section`.
- Detail tasks with names, statuses (e.g., `crit`, `done`, `active`), aliases/IDs,
  start times/dependencies (e.g., `after id`), and durations (`10d`, `24h`).
- Exclude days like `weekends` or specific dates using `excludes`.

Example with Sections and Task Dependencies:

```mermaid
gantt
    title Software Release Schedule
    dateFormat  YYYY-MM-DD
    excludes    weekends

    section Planning
    Requirements gathering :done,    req1, 2024-01-01, 7d
    Design phase           :active,  des1, after req1, 5d

    section Development
    Frontend implementation:         dev1, after des1, 10d
    Backend API integration:crit,    dev2, after des1, 14d

    section Testing & Release
    QA testing             :         qa1,  after dev2, 5d
    Deployment             :milestone, m1,  after qa1, 0d
```

Docs: <https://mermaid.js.org/syntax/gantt.html>

### GitGraph Diagrams

A GitGraph diagram visualizes Git repository structures, including branches,
commit histories, and merge strategies.

- Use `gitGraph` to layout the repository history diagram.
- Add commits to the active branch using the `commit` command. Customize
  its appearance or metadata with `id`, `tag`, or `type` (e.g., `HIGHLIGHT`).
- Create branches using `branch <name>`.
- Switch between existing branches using `checkout <name>`.
- Merge a branch into the current one using `merge <branch_name>`.

Example with Branches, Commits, and Merges:

```mermaid
gitGraph
    commit id: "Initial commit"
    branch develop
    checkout develop
    commit id: "Add feature A"
    branch feature/login
    checkout feature/login
    commit id: "Login UI"
    commit type: HIGHLIGHT id: "Fix auth bug"
    checkout develop
    merge feature/login
    checkout main
    merge develop tag: "v1.0.0"
```

Docs: <https://mermaid.js.org/syntax/gitgraph.html>

### Kanban Diagram

A Kanban diagram visualizes work at various stages of a process, using columns to
represent stages and cards to represent individual work items.

- Use `kanban` to initialize the diagram type.
- Define columns by writing the column name directly (e.g., `Todo`, `Done`).
- Add tasks underneath their corresponding column using square brackets (`[Task Name]`).
- Optionally add metadata like `id: <number>` or `assigned: <name>` indented under a task.

Example demonstrating a simple workflow with assignments:

```mermaid
kanban
  Todo
    [Plan new features]
      id: 1
      assigned: Alice
    [Design UI]
      id: 2
      assigned: Bob
  In progress
    [Develop Kanban integration]
      id: 3
      assigned: Team
  Done
    [Fix initial bugs]
```

Docs: <https://mermaid.js.org/syntax/kanban.html>

### Mindmap Diagrams

A Mindmap is a diagram used to visually organize information into a hierarchy,
showing relationships and sub-components radiating from a central concept.

- Use `mindmap` to create hierarchical diagrams such as facts stores or brainstorms.
- Establish relationships and hierarchy strictly through indentation.
- Define a central starting node (e.g., `root((Project Name))`).
- Customize node shapes using brackets like `[square]`, `(rounded)`,
  `((circle))`, or `{{hexagon}}`.

Example representing a canonical facts store:

```mermaid
%% Example canonical facts store
%% Note: Keep items in alphabetical order.
mindmap
  root((Project Name))
    Architecture
      Components
        ComponentA::Role
        ComponentB::Role
      Protocols
        ProtocolA
          Rule_1
          Rule_2
    Context
      Agents_Path::Location
      Deployment::Target_Environment
      Documentation::Location
      License::Type
      Metrics
        MetricA::Value
      Organization::Name
      Purpose::Description
    Ecosystem
      Dependencies
        LibA
        LibB
      Languages
        PrimaryLanguage::Version
      Tools
        Automation
          ToolA
        Linters
          LinterA
          LinterB
```

Docs: <https://mermaid.js.org/syntax/mindmap.html>

### Pie chart diagrams

A Pie chart is a circular statistical graphic divided into slices to
illustrate numerical proportions.

- Use `pie` to visualize parts of a whole and percentages.
- Append `showData` after the declaration (e.g., `pie showData`) to display the
  actual data values in the legend alongside their percentages.
- Define an optional `title` to describe the chart.
- Specify data slices using the format `"label" : value`.

Example with data values shown:

```mermaid
pie showData
    title Framework Popularity
    "React" : 40
    "Vue" : 30
    "Angular" : 15
    "Svelte" : 10
    "Other" : 5
```

Docs: <https://mermaid.js.org/syntax/pie.html>

### Quadrant Chart

A Quadrant chart visualizes items across a two-dimensional grid
divided into four quadrants. It is often used to evaluate or prioritize
data based on two criteria (e.g., effort versus impact).

- Use `quadrantChart` to evaluate and position items in four quadrants.
- Add an optional `title` to describe the matrix.
- Define axes using `x-axis <left> --> <right>` and `y-axis <bottom> --> <top>`.
- Assign labels to quadrants using `quadrant-1` (top right), `quadrant-2`
  (top left), `quadrant-3` (bottom left), and `quadrant-4` (bottom right).
- Place items using `"Label": [x, y]` coordinates (values between `0.0` and `1.0`).

Example with Axes, Quadrant Labels, and Points:

```mermaid
quadrantChart
    title Prioritization Matrix
    x-axis Low Effort --> High Effort
    y-axis Low Impact --> High Impact
    quadrant-1 Major Projects
    quadrant-2 Quick Wins
    quadrant-3 Time Fillers
    quadrant-4 Thankless Tasks
    "Automate Testing": [0.3, 0.8]
    "New Analytics Dashboard": [0.8, 0.9]
    "Fix Typos in README": [0.2, 0.2]
    "Refactor Legacy DB module": [0.9, 0.1]
```

Docs: <https://mermaid.js.org/syntax/quadrantChart.html>

### Requirement Diagram

A Requirement diagram provides a visualization for requirements,
components, and the connections mapping dependencies between them.

- Use `requirementDiagram` to model requirements and system element dependencies.
- Define a `requirement` block with attributes like `id` (numeric), `text`,
  `risk` (Low, Medium, High), and `verifymethod` (Analysis, Demonstration, Inspection, Test).
- Define `element` blocks to represent system components that relate to requirements.
- Use relationships to link elements and requirements applying the format
  `- <type> ->` (e.g., `satisfies`, `contains`, `derives`, `refines`).

Example with Requirements, Elements, and Relationships:

```mermaid
requirementDiagram

    requirement user_login {
    id: 1
    text: Users must be able to log in securely.
    risk: high
    verifymethod: test
    }

    requirement password_complexity {
    id: 2
    text: Passwords must be at least 8 characters.
    risk: medium
    verifymethod: inspection
    }

    element auth_module {
    type: component
    }

    password_complexity - derives -> user_login
    auth_module - satisfies -> user_login
```

Docs: <https://mermaid.js.org/syntax/requirementDiagram.html>

### Sequence Diagrams

A Sequence diagram is an interaction diagram that shows how processes operate with one another and in what order.

- Use `sequenceDiagram` for interacting components.
- Define explicitly with `participant` or `actor`, and use aliases (`actor U as User`) for concise code.
- Use `autonumber` for automatic step numbering.
- Indicate execution context with activations (`+` / `-` or `activate`/`deactivate`).
- Add logic blocks (`alt` / `else`, `opt`, `loop`).
- Group participants using `box` blocks to denote system boundaries.

Example with Actors, Grouping, Logic, and Activations:

```mermaid
sequenceDiagram
    autonumber
    actor U as User
    box LightBlue Internal System
        participant A as API Gateway
        participant S as Database
    end

    U->>+A: Request
    A->>+S: Query
    Note right of S: Processing...

    alt is found
        S-->>A: Results
    else is not found
        S-->>A: Error
    end

    deactivate S
    A-->>-U: Response
```

Example with Special Participant Types:

```mermaid
sequenceDiagram
    participant C as Boundary@{ "type" : "boundary" }
    participant S as Service
    C->>S: Request from boundary
    S->>C: Response to boundary
```

Docs: <https://mermaid.js.org/syntax/sequenceDiagram.html>

### State Diagrams

A State diagram describes the behavior of a system by representing
it as a finite number of states and the transitions between them.

- Use `stateDiagram-v2` for state machine visualization.
- Define states and use `-->` for transitions.
- Use `[*]` to represent the initial and final states.
- Describe transitions (e.g., `State1 --> State2 : Transition text`).
- Group related states logically using composite states.

Example with Transitions and Composite States:

```mermaid
stateDiagram-v2
    [*] --> Idle

    Idle --> Processing : Start

    state Processing {
        [*] --> Validating
        Validating --> Saving : Valid
        Validating --> ErrorMode : Invalid
        Saving --> [*]
    }

    Processing --> Idle : Complete
    Processing --> ErrorMode : Failed
    ErrorMode --> Idle : Reset
    ErrorMode --> [*] : Fatal
```

Docs: <https://mermaid.js.org/syntax/stateDiagram.html>

### Timeline Diagram

A Timeline diagram is a graphical representation used to display
a list of events in chronological order.

- Use `timeline` to visualize chronological events and historical progress.
- Include an optional `title` to describe the timeline's subject.
- Group events logically using `section` blocks.
- Define periods and associated events using the format
  `<time period> : <event> : <additional event>`.

Example with Sections and Multiple Events:

```mermaid
timeline
    title History of Social Media
    section 2000s
        2002 : LinkedIn
        2004 : Facebook
        2006 : Twitter
    section 2010s
        2010 : Instagram : Pinterest
        2016 : TikTok
```

Docs: <https://mermaid.js.org/syntax/timeline.html>

### User Journey Diagram

A User Journey describes at a high level of detail the exact steps
different users take to complete a specific task within a system,
application, or website.

- Use `journey` to visualize user experiences and workflows.
- Define a `title` for the overall journey.
- Divide the journey into logical stages using `section`.
- Define steps using the syntax `Task name: <score 1-7>: <Actor1>, <Actor2>`.
  The score indicates user satisfaction at that step.

Example with Sections, Scores, and Actors:

```mermaid
journey
    title Online Shopping Experience

    section Browsing
      Search for product: 5: Customer
      View product details: 4: Customer
      Read reviews: 3: Customer

    section Checkout
      Add to cart: 6: Customer
      Enter shipping info: 4: Customer
      Process payment: 5: Customer, System

    section Post-Purchase
      Receive confirmation: 6: Customer, System
      Track shipping: 5: Customer
```

Docs: <https://mermaid.js.org/syntax/userJourney.html>

## What to Avoid

- **Hardcoding Styles**: Prefer class-based styling or default themes over inline styles where possible.
- **Inconsistent Indentation**: Avoid mixing tabs and spaces. Using strict, consistent indentation is
  critical for hierarchy-based diagrams like Mindmaps, TreeViews, and Treemaps.
- **Non-standard Extensions**: Stick to core Mermaid features for maximum portability.
- **Over-complexity**: Avoid massive diagrams that are hard to render or read.
- **Unquoted Strings**: Avoid leaving strings that contain spaces or special characters unquoted to prevent parser breaks.

## Maintenance

Note that this file should be updated if Mermaid syntax changes or new useful patterns are discovered.
