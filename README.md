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

# Make the scripts executable
chmod +x mood_ring_terminal.py
chmod +x mood_ring_simple.py
chmod +x mood_ring_demo.py
```

## Usage

### Option 1: Full Interactive Version (Unix/Linux/macOS)
```bash
python3 mood_ring_terminal.py
```

### Option 2: Simplified Interactive Version (All Platforms)
```bash
python3 mood_ring_simple.py
```

### Option 3: Demo Mode (See the effects without typing)
```bash
python3 mood_ring_demo.py
```

## Requirements

- Python 3.6+
- Terminal with ANSI color support
- Unix-like system (Linux/macOS) for best experience with the full version
- Windows users: Use the simplified version for better compatibility

## How It Works

1. The application monitors your typing speed in real-time
2. Based on your typing patterns, it calculates a "mood score"
3. Different typing speeds trigger different mood states
4. Each mood state has unique ASCII patterns and colors
5. The patterns evolve and animate continuously
6. Your mood can drift over time if you stop typing

## Files in This Repository

- `mood_ring_terminal.py` - Full-featured version with real-time character input (Unix/Linux/macOS)
- `mood_ring_simple.py` - Simplified version that works on all platforms
- `mood_ring_demo.py` - Demo mode that automatically cycles through moods

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
- Use `mood_ring_terminal.py` for the best experience

### Windows
- Line-by-line input (press Enter after each line)
- May require enabling ANSI support in terminal
- Use `mood_ring_simple.py` for better compatibility

## Troubleshooting

- **Colors not showing?** Make sure your terminal supports ANSI colors
- **Windows issues?** Try running in Windows Terminal or use the simplified version
- **Permission denied?** Make the script executable with `chmod +x`

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