# Hunt the Wumpus 🐺🕳️✨

Welcome to **Hunt the Wumpus**, a classic text-based adventure game! 🏰

A 1:1 Python port of the original BASIC game from 1973.

The goal of this project is to be as similar as possible to the original source code.

![Wumpus](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Wumpus.svg/langfr-128px-Wumpus.svg.png)

## Table of Contents

- [Welcome](#welcome)
- [Rules](#rules)
  - [Hazards](#hazards)
    - [Bottomless Pits](#bottomless-pits)
    - [Super Bats](#super-bats)
  - [Wumpus](#wumpus)
  - [You](#you)
- [Warnings](#warnings)
- [How to Play](#how-to-play)
- [Installation](#installation)
- [Contribution](#contribution)
- [License](#license)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)

---

## Welcome

**WELCOME TO 'HUNT THE WUMPUS'**

The Wumpus lives in a cave of **20 rooms**. Each room has **3 tunnels** leading to other rooms. (Look at a dodecahedron to see how this works—if you don't know what a dodecahedron is, ask someone.)

### Dodecahedron Illustration

To better understand the cave layout, refer to the illustrations below:

| 3D View | 2D View |
|---------|---------|
| ![3D Dodecahedron](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Hunt_the_Wumpus_map_3d.svg/152px-Hunt_the_Wumpus_map_3d.svg.png) | ![2D Dodecahedron](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Hunt_the_Wumpus_map.svg/152px-Hunt_the_Wumpus_map.svg.png) |

---

## Rules

### Hazards

#### Bottomless Pits

- **BOTTOMLESS PITS** - Two rooms have bottomless pits in them.
  - *If you go there, you fall into the pit (& lose!)*

#### Super Bats

- **SUPER BATS** - Two other rooms have super bats.
  - *If you go there, a bat grabs you and takes you to some other room at random. (Which might be troublesome)*

### Wumpus

The Wumpus is not bothered by the hazards (he has sucker feet and is too big for a bat to lift). Usually, he is asleep. Two things wake him up: **your entering his room** or **your shooting an arrow**.

- *If the Wumpus wakes, he moves (**P=.75**) one room or stays still (**P=.25**). After that, if he is where you are, he eats you up (& you lose!)*

### You

Each turn you may **move** or **shoot a crooked arrow**.

#### Moving

- **MOVING**: You can go one room (through one tunnel)

#### Arrows

- **ARROWS**: You have **5 arrows**. You lose when you run out.
- Each arrow can go from **1 to 5 rooms**. You aim by telling the computer the room numbers you want the arrow to go to.
- If the arrow can't go that way (i.e., no tunnel) it moves **at random** to the next room.
- *IF THE ARROW HITS THE WUMPUS, YOU WIN.*
- *IF THE ARROW HITS YOU, YOU LOSE.*

---

## Warnings

When you are **one room away** from the Wumpus or a hazard, the computer says:

- **WUMPUS**: `'I SMELL A WUMPUS'`
- **BAT**: `'BATS NEARBY'`
- **PIT**: `'I FEEL A DRAFT'`

---

## How to Play

1. **Start the Game**
   - You are prompted to read the instructions. Choose **Y** to read or **N** to skip.
2. **Initialize the Cave**
   - The cave is set up with the player, Wumpus, pits, and bats in random rooms, ensuring no overlaps.
3. **Gameplay Loop**
   - **Display Location & Warnings**
     - Current room and tunnel connections are displayed.
     - Any nearby hazards are announced.
   - **Choose Action**
     - Decide to **SHOOT** an arrow or **MOVE** to another room.
4. **Shooting an Arrow**
   - Specify the number of rooms (**1-5**) the arrow will pass through.
   - Enter the sequence of room numbers for the arrow's path.
   - The arrow follows the path, checking for collisions with the Wumpus or the player.
   - If the arrow misses, the Wumpus may move.
5. **Moving to a Room**
   - Enter the room number you wish to move to.
   - If the move is valid, update your location and check for hazards.
6. **End Conditions**
   - **Win**: Shoot the Wumpus with an arrow.
   - **Lose**: Run out of arrows, fall into a pit, be eaten by the Wumpus, or hit by your own arrow.
7. **Replay Option**
   - After a game ends, choose whether to use the same cave setup or generate a new one.

---

## Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/hunt-the-wumpus.git
    ```
2. **Navigate to the Directory**
    ```bash
    cd hunt-the-wumpus
    ```
3. **Run the Game**
    ```bash
    python hunt_the_wumpus.py
    ```

---

## Contribution

Contributions are welcome! 🎉 Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes with clear messages.
4. Push to your forked repository.
5. Submit a pull request detailing your changes.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgements

- **Original Game** by **Gregory Yob** (1973).
- **1:1 Python Port** by **Sebastien Mametz** (2025).
- Special thanks to all Wumpus enthusiasts and contributors!

---

## Contact

For any questions, suggestions, or feedback, please use the [Issues](https://github.com/yourusername/hunt-the-wumpus/issues) section of this repository. Feel free to open a new issue for any inquiries related to the project.

You can also follow me on [GitHub](https://github.com/yourusername) or [Twitter](https://twitter.com/votretwitter) for updates.
