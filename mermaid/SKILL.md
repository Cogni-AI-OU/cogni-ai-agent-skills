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

### Architecture Diagrams

- Use `architecture-beta` to show system structure and relationships.

Example:

```mermaid
architecture-beta
    group api(cloud)[API]

    service db(database)[Database] in api
    service disk1(disk)[Storage] in api
    service disk2(disk)[Storage] in api
    service server(server)[Server] in api

    db:L -- R:server
    disk1:T -- B:server
    disk2:T -- B:db
```

### Block Diagrams

- Use `block-beta` to show ...

Example:

```mermaid
block-beta
columns 1
  db(("DB"))
  blockArrowId6<["&nbsp;&nbsp;&nbsp;"]>(down)
  block:ID
    A
    B["A wide one in the middle"]
    C
  end
  space
  D
  ID --> D
  C --> D
  style B fill:#969,stroke:#333,stroke-width:4px
```

### Class Diagrams

> In software engineering, a class diagram in the Unified Modeling Language (UML) is a type of static structure diagram
> that describes the structure of a system by showing the system's classes, their attributes, operations (or methods), and the relationships among objects.

- Use `classDiagram` to show ...

Example:

```mermaid
classDiagram
    Animal <|-- Duck
    Animal <|-- Fish
    Animal <|-- Zebra
    Animal : +int age
    Animal : +String gender
    Animal: +isMammal()
    Animal: +mate()
    class Duck{
      +String beakColor
      +swim()
      +quack()
    }
    class Fish{
      -int sizeInFeet
      -canEat()
    }
    class Zebra{
      +bool is_wild
      +run()
    }
```

Docs: <https://mermaid.js.org/syntax/classDiagram.html>

### Flowcharts

- Use `flowchart to show ...

Example:

  ```mermaid
flowchart TD
    Start([Start]) --> GetMoney[Get money]
    GetMoney --> GoShopping[Go shopping]
    GoShopping --> Laptop{Is it a Laptop?}
    Laptop -->|Yes| BuyLaptop[Buy Laptop]
    Laptop -->|No| BuyiPhone[Buy iPhone]
    BuyLaptop --> Stop([End])
    BuyiPhone --> Stop
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

### Entity Relationship Diagrams

> An entity–relationship model (or ER model) describes interrelated things of interest in a specific domain of knowledge.
> A basic ER model is composed of entity types (which classify the things of interest) and specifies relationships that
> can exist between entities (instances of those entity types)

- Use `erDiagram` to show ...

Example:

```mermaid
erDiagram
    CUSTOMER ||--o{ ORDER : places
    ORDER ||--|{ ORDER_ITEM : contains
    PRODUCT ||--o{ ORDER_ITEM : includes
    CUSTOMER {
        string id
        string name
        string email
    }
    ORDER {
        string id
        date orderDate
        string status
    }
    PRODUCT {
        string id
        string name
        float price
    }
    ORDER_ITEM {
        int quantity
        float price
    }
```

Docs: <https://mermaid.js.org/syntax/entityRelationshipDiagram.html>

### Gantt Charts

> A Gantt chart is a type of bar chart, first developed by Karol Adamiecki in 1896, and independently by Henry Gantt in the 1910s,
> that illustrates a project schedule and the amount of time it would take for any one project to finish.
> Gantt charts illustrate number of days between the start and finish dates of the terminal elements and summary elements of a project.

- Use `gantt` for project schedules and timelines.
- Define `dateFormat`, `title`, and `section` for organization.

Example:

```mermaid
gantt
    title A Gantt Diagram
    dateFormat  YYYY-MM-DD
    section Section
    A task           :a1, 2014-01-01, 30d
    Another task     :after a1  , 20d
    section Another
    Task in sec      :2014-01-12  , 12d
    another task      : 24d
```

Syntax:

```mermaid
gantt
    dateFormat  YYYY-MM-DD
    title       Adding GANTT diagram functionality to mermaid
    excludes    weekends
    %% (`excludes` accepts specific dates in YYYY-MM-DD format, days of the week ("sunday") or "weekends", but not the word "weekdays".)

    section A section
    Completed task            :done,    des1, 2014-01-06,2014-01-08
    Active task               :active,  des2, 2014-01-09, 3d
    Future task               :         des3, after des2, 5d
    Future task2              :         des4, after des3, 5d

    section Critical tasks
    Completed task in the critical line :crit, done, 2014-01-06,24h
    Implement parser and jison          :crit, done, after des1, 2d
    Create tests for parser             :crit, active, 3d
    Future task in critical line        :crit, 5d
    Create tests for renderer           :2d
    Add to mermaid                      :until isadded
    Functionality added                 :milestone, isadded, 2014-01-25, 0d

    section Documentation
    Describe gantt syntax               :active, a1, after des1, 3d
    Add gantt diagram to demo page      :after a1  , 20h
    Add another diagram to demo page    :doc1, after a1  , 48h

    section Last section
    Describe gantt syntax               :after doc1, 3d
    Add gantt diagram to demo page      :20h
    Add another diagram to demo page    :48h
```

Docs: <https://mermaid.js.org/syntax/gantt.html>

### Mindmap Diagrams

- Use `mindmap` for hierarchical information and brainstorming.

Example:

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

### Sequence Diagrams

- Use `sequenceDiagram` for interacting components.
- Utilize `participant` and `actor` for clarity.
- Use `autonumber` for step-by-step flows.

Examples:

```mermaid
sequenceDiagram
  autonumber
  Alice->>Bob: Hello Bob, how are you?
  Bob-->>Alice: I am good thanks!
```

```mermaid
sequenceDiagram
    participant Alice
    participant Bob
    Bob->>Alice: Hi Alice
    Alice->>Bob: Hi Bob
```

```mermaid
sequenceDiagram
    participant Alice@{ "type" : "boundary" }
    participant Bob
    Alice->>Bob: Request from boundary
    Bob->>Alice: Response to boundary
```

Docs: <https://mermaid.js.org/syntax/sequenceDiagram.html>

### State Diagrams

> A state diagram is a type of diagram used in computer science and related fields to describe the behavior of systems.
> State diagrams require that the system described is composed of a finite number of states; sometimes, this is indeed the case,
> while at other times this is a reasonable abstraction.

- Use `stateDiagram-v2` for state machine visualization.

Example:

```mermaid
stateDiagram-v2
    [*] --> Still
    Still --> [*]
    Still --> Moving
    Moving --> Still
    Moving --> Crash
    Crash --> [*]
```

Docs: <https://mermaid.js.org/syntax/stateDiagram.html>

### User Journey Diagram

> User journeys describe at a high level of detail exactly what steps different users take to complete a specific task within a system,
> application or website. This technique shows the current (as-is) user workflow, and reveals areas of improvement for the to-be workflow.

- Use `journey` for state machine visualization.

Example:

```mermaid
journey
    title My working day
    section Go to work
      Make tea: 5: Me
      Go upstairs: 3: Me
      Do work: 1: Me, Cat
    section Go home
      Go downstairs: 5: Me
      Sit down: 5: Me
```

Docs: <https://mermaid.js.org/syntax/userJourney.html>

## What to Avoid

- **Over-complexity**: Avoid massive diagrams that are hard to render or read.
- **Non-standard Extensions**: Stick to core Mermaid features for maximum portability.
- **Hardcoding Styles**: Prefer class-based styling or default themes over inline styles where possible.

## Maintenance

Note that this file should be updated if Mermaid syntax changes or new useful patterns are discovered.
