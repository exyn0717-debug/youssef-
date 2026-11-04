# CSE013 — Complete IT Study Summary

**Intro to Information Systems & Technology · Engineering Information Systems and Digital Skills**

Four lectures · 187 slides. **English — the original language of the uploaded PDFs, not translated.** Every factual line below is a verbatim sentence or phrase from those slides; only the arrangement, headings, tables, grouping and study aids are editorial. Source pages are listed under each section, and the four file hashes are recorded below so any line can be checked against its original.

## At a glance

### What the four lectures cover

- An Information System combines people, hardware, software, data, and networks.
- Performance depends on the whole system, not one specification alone.
- Managing an organization’s data resources so people and systems can find and use the information they need.
- Base determines the digit set and place values. Binary is base 2; decimal base 10; octal base 8; hexadecimal base 16. Convert using place values, repeated division or bit grouping.

### Subject map

| Lecture | Pages | Big question | One thing you must be able to do |
|---|---|---|---|
| L1 · Information Systems | 24 | What is an Information System? | Define an Information System (IS) and distinguish IS from Information Technology (IT). |
| L2 · Hardware & Software | 43 | What is a computer system? | Explain the roles of the CPU, ALU, Control Unit, registers, cache, RAM and storage. |
| L3 · Data Resource Management | 82 | What is data resource management? | Explain why organizations need reliable, well-managed data. |
| NUM · Number Systems & ASCII | 38 | What is a number system? | Explain decimal, binary, octal and hexadecimal; convert between bases. |

### How the pieces connect

- Information systems connect people, technology, data, and processes.
- Hardware and software work together in engineering environments.
- Reliable decisions depend on reliable data.
- Digital circuits can reliably represent two states.

### Sources — the four uploaded files

| Original file | Stored as | Pages | SHA-256 |
|---|---|---|---|
| `IT_lecture_1_2026.pdf` | `cse013-lecture-1-intro.pdf` | 24 | `37da860d2583855af8860a7a26acfa7ea4646511e4f1e1ea6a589621079b7837` |
| `IT_lecture_2_2026.pdf` | `cse013-lecture-2-hardware.pdf` | 43 | `ff51f5a3d302ec497cd5a8c876d9e86ee90cf2cbfff0bb00b537a33e8484a50a` |
| `IT_lecture_3_2026.pdf` | `cse013-lecture-3-data.pdf` | 82 | `80f0e7fafdc44d17bf98741bf8f1d8047fbff1d795047c2d71357536e340880e` |
| `IT_Number_Systems.pdf` | `cse013-number-systems.pdf` | 38 | `bcaaebb307299a7ca5963df121644386d191a023dad3aba82733056c45dec38b` |

## Lecture 1 | Introduction to Information Systems

*Source: `IT_lecture_1_2026.pdf`, pp. 4–23*

### In one line

> Key idea: an IS is more than a computer or a software application.

### What you must be able to do

- Define an Information System (IS) and distinguish IS from Information Technology (IT).
- Identify the five major resources of an information system.
- Explain the basic activities of an information system.
- Recognize major types of information systems used by organizations.
- Explain why information systems matter to engineers.
- Identify ethical challenges associated with the use of information technology.

### From system to information system

| Concept | What the slides say |
|---|---|
| System | A system is a group of interrelated components working together toward a common goal. |
| Boundary | A system has a defined boundary and interacts with its environment. |
| Definition of IS | An organized combination of people, hardware, software, communications networks, and data resources that stores, retrieves, transforms, and disseminates information. |

- Input — capturing and assembling elements that enter the system
- Processing — transforming inputs into outputs
- Output — delivering the results to their destination
- Feedback and control — monitoring performance and guiding the system

*Source: `IT_lecture_1_2026.pdf`, p. 4, p. 6*

### IS vs IT — the distinction students lose marks on

|  | Information Systems (IS) | Information Technology (IT) |
|---|---|---|
| Scope | Information Systems (IS) is a broader framework that combines that technology with people, data, and business processes to achieve organizational goals | Information Technology (IT) focuses on the physical tools and infrastructure (like hardware, software, and networks) |
| Contains | Includes people, processes, hardware, software, data, and networks. | Includes hardware, software, networks, and related technologies. |
| Focus | Focuses on how these elements work together. | IT is a major part of an information system—not the whole system. |

*Source: `IT_lecture_1_2026.pdf`, p. 7*

### The five major IS resources

| Resource | What it means |
|---|---|
| People | Users & specialists |
| Hardware | Physical devices |
| Software | Instructions & programs |
| Data | Facts & observations |
| Networks | Communication resources |

### What an information system does

Example: University registration → student data entered → system processes registration → timetable/records produced → data stored → rules and checks control the process.

*Source: `IT_lecture_1_2026.pdf`, pp. 8–9*

### Types of information systems

| Family | Systems named in the slides | What they support |
|---|---|---|
| Operations Support Systems | Transaction Processing Systems (TPS) | Support day-to-day operations and transactions. |
| Operations Support Systems | Process Control Systems (PCS) |  |
| Operations Support Systems | Enterprise Collaboration Systems |  |
| Management Support Systems | Management Information Systems (MIS) | Support analysis, reporting, and decision making. |
| Management Support Systems | Decision Support Systems (DSS) |  |
| Management Support Systems | Executive Information Systems (EIS) |  |

A Transaction Processing System (TPS) is a software-based information system that collects, stores, modifies, and retrieves routine daily business transactions.

A Process Control System (PCS) is an industrial automation network that monitors and regulates physical variables like temperature, pressure, and flow rates to keep manufacturing and production facilities running safely and efficiently

*Source: `IT_lecture_1_2026.pdf`, pp. 11–16*

### Why engineers need this

- Engineering work is increasingly connected to digital information and networked systems.
- Engineers use information systems for design, manufacturing, maintenance, project management, communication, and decision making.
- Understanding IS helps engineers communicate effectively with IT specialists and other organizational functions.

### Ethical challenges to name

- Privacy — who should have access to personal or organizational data?
- Accuracy — how do we ensure that information is correct and reliable?
- Intellectual property — who owns software, data, images, and digital content?
- Security — how do we protect systems and information from misuse?
- Responsible use — how should people behave when using organizational technology?

*Source: `IT_lecture_1_2026.pdf`, pp. 10, 18–19*

### Exam focus

- An Information System combines people, hardware, software, data, and networks.
- IS transforms data into useful information through input, processing, output, storage, and control.
- Information systems support both organizational operations and management decision making.
- Engineers interact with information systems throughout their education and professional careers.
- Technology must be used effectively, securely, and ethically.

### Exit ticket — can you answer these?

- 1. What is the difference between an Information System and Information Technology?
- 2. Name the five major IS resources.
- 3. Give one example of an Information System used by an engineer.
- 4. Identify one ethical issue related to information technology.
- 5. In one sentence: Why does an engineer need to understand Information Systems?

*Source: `IT_lecture_1_2026.pdf`, pp. 20, 23*

## Lecture 2 | Computer Hardware, Software & Architecture

*Source: `IT_lecture_2_2026.pdf`, pp. 4–43*

### In one line

> A computer system is more than a CPU.

### What you must be able to do

- Identify the main functional components of a computer system.
- Explain the roles of the CPU, ALU, Control Unit, registers, cache, RAM and storage.
- Describe the instruction cycle and the purpose of buses.
- Explain the memory hierarchy and basic factors affecting performance.
- Distinguish system software from application software.
- Recognize the roles of operating systems, programming languages and translation tools.
- Connect hardware and software to common engineering applications.

### The five functional groups

| Group | Job | Examples |
|---|---|---|
| 1 INPUT | Receives data and commands | Keyboard • mouse • scanner |
| 2 PROCESSING | Transforms data | CPU • ALU • Control Unit |
| 3 MEMORY & STORAGE | Holds active data and saved files | RAM • cache • SSD • HDD |
| 4 OUTPUT | Presents results | Monitor • printer • display |
| CONTROL | CONTROL CPU and system software coordinate system activities. |  |

*Source: `IT_lecture_2_2026.pdf`, p. 5*

### Inside the CPU — who does what

| Part | What it does |
|---|---|
| CPU | Executes instructions and coordinates processing. |
| ALU | The ALU performs arithmetic and logical operations required by instructions. |
| Control Unit | It manages the sequence; it does not perform the main arithmetic calculations. |
| Registers | Very small storage locations inside the CPU. • Hold data, instructions, addresses or intermediate results. • Give the CPU immediate access to information it is using. |
| Cache | High-speed memory close to the CPU. • Stores frequently used data and instructions. • Reduces CPU waiting time. • Smaller than RAM, but typically faster. |

*Source: `IT_lecture_2_2026.pdf`, pp. 7–11*

### The instruction cycle

| Stage | What happens |
|---|---|
| 1 FETCH | The CPU obtains the next instruction from memory. |
| 2 DECODE | The instruction is interpreted to determine what is required. |
| 3 EXECUTE | The CPU performs the required operation. |
| 4 STORE / UPDATE | The result is stored or the program state is updated. |

The cycle repeats while a program runs.

*Source: `IT_lecture_2_2026.pdf`, p. 12*

### Buses

| Bus | Job |
|---|---|
| DATA BUS | Carries data between components. |
| ADDRESS BUS | Identifies the location being accessed. |
| CONTROL BUS | Carries signals that coordinate operations. |

*Source: `IT_lecture_2_2026.pdf`, p. 13*

### Memory vs storage — the classic contrast

|  | Memory (RAM and cache) | Storage (SSD and HDD) |
|---|---|---|
| Role | Supports programs while they are running. • Fast access to active data. • RAM is usually volatile: its contents are lost when power is off. | Keeps files and programs long term. • Retains information when power is off. • Usually has more capacity than RAM. • SSDs have no moving parts and are generally faster than HDDs. |
| Speed / size | Cache is smaller and closer to the CPU. | Usually has more capacity than RAM. |
| Volatility | RAM is usually volatile: its contents are lost when power is off. | Retains information when power is off. |

### Memory hierarchy (fastest → largest)

| Level | What the slides say |
|---|---|
| REGISTERS | Smallest and fastest; inside the CPU. |
| CACHE | Very fast; keeps frequently used data near the CPU. |
| RAM | Larger working area for active programs and data. |
| SSD / HDD | Long-term storage; usually larger but slower than RAM. |

In general, moving closer to the CPU means faster access and smaller capacity.

*Source: `IT_lecture_2_2026.pdf`, pp. 14–15*

### Architecture vs organization

| Term | What it describes | Examples |
|---|---|---|
| Computer architecture | The features visible to a programmer or system designer. | Instruction set |
| Computer organization | How the hardware is arranged to implement the architecture. | CPU components and internal connections |

*Source: `IT_lecture_2_2026.pdf`, p. 6*

### Performance and cores

- Performance depends on the whole system, not one specification alone.
- Multiple cores can support work in parallel when software allows it.
- More cores do not automatically make every program faster.
- Both approaches are used in real processors; performance depends on the complete design.

*Source: `IT_lecture_2_2026.pdf`, pp. 19–21*

### Software: system vs application

| Type | What it does | Examples |
|---|---|---|
| System software | Manages computer resources and provides a platform for applications. | Examples: operating systems, utilities and device drivers. |
| Application software | Helps users complete specific tasks. | Examples: CAD, spreadsheets, browsers, MATLAB and engineering simulation tools. |

### Operating system — main functions

- Provides a user interface.
- Manages processes and tasks.
- Allocates memory.
- Organizes files and storage.
- Manages devices.
- Supports security and access control.

*Source: `IT_lecture_2_2026.pdf`, pp. 22–24*

### Programming languages and translation tools

| Tool / level | What the slides say |
|---|---|
| Programming language | A formal way to give instructions to a computer. |
| Machine language | Instructions represented at the machine level; difficult for humans to write. |
| Assembly language | Uses symbolic instructions and is closely related to hardware. |
| High-level languages | Closer to human language and easier to use for complex applications. |
| COMPILER | Translates a program into a form that can be executed. |
| INTERPRETER | Reads and executes program instructions during execution. |
| ASSEMBLER | Translates assembly-language instructions into machine code. |
| PYTHON | A good introductory choice for data analysis, automation and AI. |
| C / C++ | Efficient and widely used for embedded systems and hardware- oriented applications. |
| MATLAB | Useful for numerical computing, matrices, modelling, simulation and data analysis. |

*Source: `IT_lecture_2_2026.pdf`, pp. 26–29*

### Worked example — temperature-control system

1. A temperature sensor measures the process.
2. An interface sends the measurement to a controller.
3. The program compares the value with a target or limit.
4. A display shows the result; a controller may activate an actuator.

Hardware collects and acts on signals; software defines the decision logic.

*Source: `IT_lecture_2_2026.pdf`, p. 32*

### Exam focus

- A computer system combines input, processing, memory/storage, output and control.
- The CPU uses the ALU, Control Unit, registers and cache to execute instructions.
- The instruction cycle includes fetching, decoding and executing instructions.
- Memory supports active work; storage keeps files long term.
- Operating systems manage resources; applications perform tasks.
- Programming tools support analysis, simulation, automation and embedded systems.
- Engineering performance depends on the complete hardware–software system.

*Source: `IT_lecture_2_2026.pdf`, p. 42*

## Lecture 3 | Data Resource Management

*Source: `IT_lecture_3_2026.pdf`, pp. 4–80*

### In one line

> Managing an organization’s data resources so people and systems can find and use the information they need.

### What you must be able to do

- Explain why organizations need reliable, well-managed data.
- Distinguish characters, fields, records, files and databases.
- Explain the problems of separate file-processing systems.
- Describe the role of a Database Management System (DBMS).
- Recognize database types, data warehouses and data mining.
- Read a simple relational table and understand keys and relationships.
- Explain basic steps in planning and developing a database.

### From raw data to a decision

| Step | What the slides say |
|---|---|
| DATA | Individual facts or measurements. |
| PROCESSING | Organizing, checking, combining or calculating data. |
| INFORMATION | A meaningful result. |
| DECISION | Use the information to choose an action, such as checking a cooling system. |

Reliable decisions depend on reliable data.

*Source: `IT_lecture_3_2026.pdf`, p. 5*

### The data hierarchy — small to large

| Level | Definition |
|---|---|
| CHARACTER | One symbol, such as A, 7 or #. |
| FIELD | One item of information, such as Student_ID or Temperature. |
| RECORD | A group of related fields describing one item or event. |
| FILE / DATABASE | A file groups related records; a database organizes related data for shared use. |

### Entities, attributes and relationships

| Term | Definition |
|---|---|
| Entity | A person, place, object or event about which data is stored. |
| Attribute | A characteristic of an entity. |
| Relationship | A student can enrol in several courses, and a course can include many students. |

*Source: `IT_lecture_3_2026.pdf`, pp. 6, 9–10*

### What a database is

- Data is arranged in a planned structure.
- Data elements connect to a common topic or process.
- Different users or applications can access appropriate data.
- Data can be added, updated, searched and protected.

### Traditional file processing — the four problems

| Problem | What it means |
|---|---|
| REDUNDANCY | The same data is stored more than once. |
| INCONSISTENCY | Copies may show different values after updates. |
| LIMITED SHARING | Combining information from separate files can be difficult. |
| DATA DEPENDENCE | A change in file structure may require changes to programs. |

### The DBMS answer

| DBMS task | What the slides say |
|---|---|
| Definition | Software that helps create, maintain, query and control access to a database. |
| QUERY | Ask for selected data that meets conditions. |
| REPORT | Present results in a structured format. |
| MAINTAIN | Add new records and correct existing values. |
| DEVELOP | Support applications that use the database. |
| Query | A request to retrieve data. |
| Report | A formatted presentation of information. |

A DBMS is the software layer between users/applications and the database.

*Source: `IT_lecture_3_2026.pdf`, pp. 13–21*

### Database types, warehouse, marts and mining

| Concept | What the slides say |
|---|---|
| Operational database | Stores detailed data needed for day-to-day operations. |
| Distributed / external | Distributed: data is stored or replicated across connected sites. External: data is obtained from outside sources or services. |
| Hypermedia database | Linked pages or items that may include text, images, audio, video and other media. |
| Data warehouse | A large repository that brings data together from different operational and other sources for analysis. |
| Data mart | A focused subset of data for a particular department or topic. |
| Data mining | Analyzing large collections of data to identify patterns or trends. |

*Source: `IT_lecture_3_2026.pdf`, pp. 22–28*

### Structures and keys

| Topic | What the slides say |
|---|---|
| Relational | Data is organized in tables made of rows and columns. |
| Hierarchical | Hierarchical: tree-like relationships. |
| Network | Network: records can have multiple links. |
| Object-oriented | Object-oriented: supports complex objects and associated operations. |
| Primary key | A field (or set of fields) that uniquely identifies each record. |
| Foreign key | A field that refers to a key in another table to connect related records. |

Keys help link records while keeping data organized.

*Source: `IT_lecture_3_2026.pdf`, pp. 30–35*

### Building a database

| Stage | What the slides say |
|---|---|
| PLAN | Identify users, tasks and information needs. |
| MODEL | Define entities, attributes, keys and relationships. |
| BUILD & TEST | Create the structure, enter test data and check queries. |
| MAINTAIN | Correct data, manage access, back up and improve the system. |

### Quality, views and protection

| Topic | What the slides say |
|---|---|
| Metadata | Data about data. |
| Data dictionary | A catalog describing data fields, formats, meanings, allowed values and relationships. |
| Logical view | What data is stored and how the data elements relate. |
| Physical view | How the database is stored and accessed by the computer system. |
| Data quality | A database cannot make poor input data trustworthy by itself. |
| Responsible access | Give users only the access they need. |

*Source: `IT_lecture_3_2026.pdf`, pp. 37–41*

### Exam focus

- Data resource management organizes data so people can use it reliably.
- Characters, fields, records, files and databases are related levels of data organization.
- Separate files can create duplication, inconsistency, limited sharing and data dependence.
- A DBMS supports database creation, maintenance, queries, reports and access control.
- Relational databases use tables connected by keys and relationships.
- Data warehouses support analysis; data mining looks for useful patterns.
- Database planning, modeling, testing, quality and protection are all important.

*Source: `IT_lecture_3_2026.pdf`, p. 79*

## Number Systems, Binary & ASCII

*Source: `IT_Number_Systems.pdf`, pp. 3–37*

### In one line

> Base determines the digit set and place values. Binary is base 2; decimal base 10; octal base 8; hexadecimal base 16. Convert using place values, repeated division or bit grouping.

### What you must be able to do

- Explain decimal, binary, octal and hexadecimal; convert between bases.
- Explain ASCII and distinguish it from Unicode.

### Bits, bytes and words

| Term | What the slides say |
|---|---|
| Bit | Bit: one binary digit, 0 or 1. |
| Nibble | Nibble: 4 bits. |
| Byte | Byte: 8 bits. |
| Word | A word is the natural data size a processor handles as a unit. Word size depends on processor design; common examples are 32-bit and 64-bit architectures. |
| Two states | ON/OFF; HIGH/LOW voltage; TRUE/FALSE. These states can be represented by 1 and 0. |

*Source: `IT_Number_Systems.pdf`, pp. 3–4*

### The four bases at a glance

| System | Base | Digits / place values |
|---|---|---|
| Decimal | 10 | Decimal uses digits 0 to 9. |
| Binary | 2 | Binary uses only 0 and 1. |
| Octal | 8 | Octal uses digits 0 to 7. |
| Hexadecimal | 16 | Hexadecimal uses 16 symbols: 0–9 and A–F. |

The value stays the same; only the representation changes. Use a base label when comparing systems.

*Source: `IT_Number_Systems.pdf`, pp. 5–7, 14–15, 19*

### Equivalent values — memorise this row

| Decimal | Binary | Octal | Hexadecimal |
|---|---|---|---|
| Decimal: 26₁₀ | Binary: 11010₂ | Octal: 32₈ | Hexadecimal: 1A₁₆ |

### Conversion recipes

| Goal | Method / worked example |
|---|---|
| Binary → decimal | 1×16 + 1×8 + 0×4 + 1×2 + 0×1 = 26₁₀ |
| Decimal → binary | Use repeated division by 2 and record remainders. |
| Decimal → binary (check) | 10110₂ = 16 + 0 + 4 + 2 + 0 = 22₁₀. Always convert back to check. |
| Binary → hex | Each group of four bits maps to one hex digit. |
| Binary → octal | Group binary digits into sets of three. |
| Hex → binary | 3A₁₆: 3=0011; A=1010. So 3A₁₆ = 00111010₂. Leading zeros can show complete groups. |
| Octal → binary | 47₈: 4=100; 7=111. So 47₈ = 100111₂. |

Correct: 4 for hex, 3 for octal.

*Source: `IT_Number_Systems.pdf`, pp. 8–10, 16–18, 30*

### Binary arithmetic and fractions

- 0+0=0
- 0+1=1
- 1+0=1
- 1+1=10₂
- For 1+1, write 0 and carry 1.
- 1×2¹ + 0×2⁰ + 1×2⁻¹ = 2.5₁₀. Some decimal fractions repeat in binary.

*Source: `IT_Number_Systems.pdf`, pp. 12–13*

### ASCII, Unicode and how text is stored

| Topic | What the slides say |
|---|---|
| Definition | ASCII is a character-coding standard assigning numeric codes to English letters, digits, punctuation and control characters. |
| Range | Standard ASCII uses 7 bits, giving 128 values: 0–127. Codes 0–31 and 127 are control codes; printable characters include letters, digits and punctuation. |
| Key codes | A = 65; B = 66; Z = 90 |
| Lowercase | a = 97; b = 98; z = 122 |
| Digits | 0 = 48; 1 = 49 |
| Space | Space = 32 |
| Character ≠ number | Digits 0–9 are consecutive codes. A–Z are consecutive. a–z are consecutive. Character “5” is not the same as numeric value 5. |
| ASCII limitation | Standard ASCII covers a limited set, mainly English text and control functions. It does not include most Arabic letters or many other writing systems. |
| Unicode | Unicode assigns code points across many writing systems and symbols. |
| UTF-8 | UTF-8 is a widely used Unicode encoding; ASCII characters use the same byte values in UTF-8. |
| Stored text | O → ASCII 79 → binary 01001111 |
| Encoding definition | Character encoding maps characters—letters, digits and punctuation— to numeric code values that can be stored and processed. |

*Source: `IT_Number_Systems.pdf`, pp. 20–26*

### Ranges and the mistakes examiners set

- With n bits, an unsigned number represents 0 to 2ⁿ−1.
- 8 bits: 0–255
- 16 bits: 0–65,535
- For n-bit two’s-complement integers, range is −2ⁿ⁻¹ to 2ⁿ⁻¹−1. For 8 bits: −128 to +127.
- Correct: 4 for hex, 3 for octal.
- Confusing character code with numeric value; assuming standard ASCII includes Arabic or all accented letters; assuming every encoding always uses one byte.

*Source: `IT_Number_Systems.pdf`, pp. 27–28, 30*

### Method reminders + exam focus

- Binary→decimal: add active powers of 2. Decimal→binary: repeated division or powers of 2. Hex→decimal: powers of 16. Binary→octal: groups of 3. Binary→hex: groups of 4.
- Computers represent data using bits. ASCII maps a limited character set to codes. Unicode supports many writing systems. The same bits can have different meanings depending on the format.
- Exit ticket: convert 100101₂ to decimal and explain one difference between ASCII and Unicode.

*Source: `IT_Number_Systems.pdf`, pp. 32, 37*

## Cheat sheet

Everything on this page is verbatim from the slides — a last-minute revision card.

### Lecture 1 — five resources / five activities

| Five IS resources | Five IS activities |
|---|---|
| PEOPLE | INPUT |
| HARDWARE | PROCESS |
| SOFTWARE | OUTPUT |
| DATA | STORAGE |
| NETWORKS | CONTROL |

### Lecture 2 — CPU, cycle, buses

| Item | One-line answer |
|---|---|
| ALU | The ALU performs arithmetic and logical operations required by instructions. |
| Control Unit | It manages the sequence; it does not perform the main arithmetic calculations. |
| Instruction cycle | 1 FETCH · 2 DECODE · 3 EXECUTE · 4 STORE / UPDATE |
| Buses | A bus is a communication path inside a computer. |
| Memory hierarchy | Registers → Cache → RAM → SSD / HDD |
| RAM vs storage | RAM is usually volatile: its contents are lost when power is off. |

### Lecture 3 — hierarchy and keys

| Item | One-line answer |
|---|---|
| Hierarchy | CHARACTER → FIELD → RECORD → FILE / DATABASE |
| Primary key | A field (or set of fields) that uniquely identifies each record. |
| Foreign key | A field that refers to a key in another table to connect related records. |
| 4 file problems | REDUNDANCY · INCONSISTENCY · LIMITED SHARING · DATA DEPENDENCE |
| DBMS | Software that helps create, maintain, query and control access to a database. |

### Number systems — the table to remember

| Base | Digits | Example |
|---|---|---|
| 2 Binary | Binary uses only 0 and 1. | Binary: 11010₂ |
| 8 Octal | Octal uses digits 0 to 7. | Octal: 32₈ |
| 10 Decimal | Decimal uses digits 0 to 9. | Decimal: 26₁₀ |
| 16 Hex | Hexadecimal uses 16 symbols: 0–9 and A–F. | Hexadecimal: 1A₁₆ |

| ASCII | Decimal code |
|---|---|
| Space | Space = 32 |
| 0 / 1 | 0 = 48; 1 = 49 |
| A / Z | A = 65; B = 66; Z = 90 |
| a / z | a = 97; b = 98; z = 122 |

| Unsigned range | Values |
|---|---|
| 4 bits | 4 bits: 0–15 |
| 8 bits | 8 bits: 0–255 |
| 16 bits | 16 bits: 0–65,535 |

### Common confusions — do not mix these up

| Do not confuse | The slides say |
|---|---|
| ALU vs Control Unit | It manages the sequence; it does not perform the main arithmetic calculations. |
| IS vs IT | IT is a major part of an information system—not the whole system. |
| Memory vs storage | Think: active working space versus long-term retention. |
| ASCII vs Unicode | Standard ASCII covers a limited set, mainly English text and control functions. It does not include most Arabic letters or many other writing systems. |
| Hex vs octal grouping | Correct: 4 for hex, 3 for octal. |
| Character "5" vs value 5 | Digits 0–9 are consecutive codes. A–Z are consecutive. a–z are consecutive. Character “5” is not the same as numeric value 5. |
| Query vs report | Queries retrieve selected data; reports present results for people to review. |

## Practice & answer keys

Where the practice and worked answers live in the original PDFs. The 59 CSE013 questions in the platform question bank come from these pages.

| Lecture | Practice pages | Answer key / worked answers |
|---|---|---|
| L1 | pp. 21–23 (activities, quick practice, exit ticket) | Open-ended exit ticket — no MCQ key |
| L2 | pp. 33–34, 35–40 (review MCQs) | p. 41 |
| L3 | pp. 70–71, 72–77 (review MCQs) | p. 78 |
| Number systems | pp. 31, 34–35 (guided practice + quick quizzes) | pp. 32–33, 36 |

### Worked answers to check your method

- 1. 101101₂ = 45₁₀
- 2. 37₁₀ = 100101₂
- 3. 7B₁₆ = 7×16 + 11 = 123₁₀
- 4. 110111₂ = 67₈
- 5. 10101111₂ = AF₁₆
- 6. A=65; a=97.
- 7. A = 01000001 (8-bit).
- 8. ASCII is a limited 7-bit standard; Unicode covers many writing systems.
- 9. 2⁸ = 256 values (0–255).
- 10. Examples: sensor readings, embedded controllers, communication or file storage.

*Source: `IT_Number_Systems.pdf`, pp. 32–33*
