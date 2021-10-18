# System Architecture Design Challenge
## Drinking Robot


## Description
Here is a technical description of the different nodes/actions/services the __Drinking Robot__ will execute. 


## Table of contents

- [Project Name](#project-name)
  - [Description](#description)
  - [Table of contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Development team](#development-team)
  - [References/Support links](#references-support-links)
  - [License](#license) 

## Env setup
1. Install ROS Noetic
2. 

## Installation

1. Clone the project repository on your local machine.

   SSH:

   ```bash
   $ git clone https://github.com/RoBorregos/Candidates-2021.git
   ```

2. Change to branch systemArchitectureChallenge

   ```bash
   $ git checkout systemArchitectureChallenge
   ```

## Robot modules

### Env analysis
Node publisher in charge of telling the robotic system what is happening around the robot.

| Topic name | Message | Definition |
| --- | --- | --- |
| env_analysis_feedback | uint16 data | <ul><li>0 - There is no stimuli</li><li>1 - Person asked for yor attention</li><li>2 - The cup is in front of you</li></ul> |

### Beverage dispenser
Action server in charge of activating and deactivating the beverage dispenser.

| Goal message | Valid goals |
| --- | --- |
| **uint16 beverage\_type**: Specifies the type of beverage the user wants. | <ul><li>1 - Lemonade</li><li>2 - Coca Cola</li><li>3 - Water</li></ul> |

### HRI
Service for human robot interaction through speech, which:
- Asks what kind of beverage the person wants.
- Retrieves the beverage

| Request | Response |
| --- | --- |
| **uint16 question**: Specifies the question the robot will give the user. <ul><li>0 - What beverage do you want?</li><li>1 - Could you repeat the beverage, please?</li></ul>|<ul><li>1 - Lemonade</li><li>2 - Coca Cola</li><li>3 - Water</li><li>4 - Undefined</li></ul> |

### Party Navigation
| Goal message | Valid goals |
| --- | --- |
| **uint16 behavior**: Specifies the navigation behavior of the robot. | <ul><li>1 - Patrol the party</li><li>2 - Stop</li></ul> |

## Development team

| Name                    | Email                                                               | Github                                                       | Role      |
| ----------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------ | --------- |
| Aurora Tijerina | [auro.tj@gmail.com](mailto:auro.tj@gmail.com) | [@AuroTB](https://github.com/aurotb) | Navigation & Integration |
| José Cisneros | [A01283070@itesm.mx](mailto:A01283070@itesm.mx) | [@Josecisneros001](https://github.com/Josecisneros001) | PM & Programmer |


## References/Support links

- [Support CODEOWNERS](https://docs.github.com/es/github/creating-cloning-and-archiving-repositories/about-code-owners)
- [Creating a pull request template](https://docs.github.com/es/github-ae@latest/github/building-a-strong-community/creating-a-pull-request-template-for-your-repository)
- [Branch naming convention](https://deepsource.io/blog/git-branch-naming-conventions/)

## License
License used.
