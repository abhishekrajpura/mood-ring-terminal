# Mood Ring Terminal 🎨

An interactive ASCII art generator that creates evolving patterns based on your typing speed and "digital mood". Just like a mood ring changes colors based on temperature, this terminal application changes its patterns and colors based on how you type!

## Features

- **Real-time Mood Detection**: Analyzes your typing speed to determine your current "digital mood"
- **Dynamic ASCII Art**: Generates evolving patterns that change based on your mood
- **Color-coded Moods**: Each mood has its own color scheme
- **Live Updates**: The display updates in real-time as you type
- **Mood Evolution**: Your mood score evolves based on typing patterns and time

## Mood States

- 🔴 **Excited** (Red) - Fast typing, high energy
- 🟡 **Happy** (Yellow) - Moderate-fast typing, positive vibes
- 🟢 **Calm** (Green) - Steady, relaxed typing
- 🔵 **Neutral** (Blue) - Average typing speed
- 🟣 **Thoughtful** (Magenta) - Slow, deliberate typing
- 🟦 **Mysterious** (Cyan) - Variable patterns

## Installation

```bash
# Clone the repository
git clone https://github.com/abhishekrajpura/mood-ring-terminal.git
cd mood-ring-terminal

# Make the script executable
chmod +x mood_ring_terminal.py

# Run the application
python3 mood_ring_terminal.py
```

## Requirements

- Python 3.6+
- Terminal with ANSI color support
- Unix-like system (Linux/macOS) for best experience
- Windows users: Works with limited functionality

## How It Works

1. The application monitors your typing speed in real-time
2. Based on your typing patterns, it calculates a "mood score"
3. Different typing speeds trigger different mood states
4. Each mood state has unique ASCII patterns and colors
5. The patterns evolve and animate continuously
6. Your mood can drift over time if you stop typing

## Usage

1. Run the script: `python3 mood_ring_terminal.py`
2. Start typing anything that comes to mind
3. Watch as the patterns and colors change based on your typing speed
4. Type 'quit' and press Enter to exit

## Technical Details

- Uses threading for real-time display updates
- Implements a deque for rolling average of typing speeds
- Terminal raw mode for character-by-character input (Unix)
- ANSI escape codes for colors and cursor control
- Pattern generation using mathematical functions and randomization

## Platform Notes

### Linux/macOS
- Full functionality with character-by-character input
- Smooth real-time updates

### Windows
- Line-by-line input (press Enter after each line)
- May require enabling ANSI support in terminal

## Contributing

Feel free to fork, modify, and submit pull requests! Some ideas for enhancements:
- Add more mood states
- Create different pattern algorithms
- Add sound effects
- Export mood history
- Multi-user mood sharing

## License

MIT License - feel free to use this in your own projects!

## Author

Created with 💜 by Abhishek Rajpura

---

*Remember: Your typing reveals your digital soul! 🌟*