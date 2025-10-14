# ATutor

This repo ain't your grandma's assembly tutor—it's a gut-punch variant for HLA
(High Level Assembly) to teach you low-level shit without drowning in pure ASM
hell. Cooked up to make you actually understand what's under the hood when
you're not just scripting "hello world" in Python. Lessons start basic: Hello
World, variables, that crap. But it builds to make you less of a high-level
poser. If you're still scared of assembly in 2025, GTFO and install HLA
already—your Omarchy box is begging for it.

## Requirements
- Python 3.x (because who the hell is still on 2? Fix your shit. On Omarchy:
  pacman -S python if you're that lost.)
- Vim (duh. If you don't have it, `sudo pacman -S vim`. This ain't Notepad
  territory.)
- HLA (High Level Assembler). See the installation section below—no separate
  file, because who needs extra clutter? Follow it or weep when hla bitches
about paths.

## Installing HLA on Omarchy Listen up, you lazy bastard—HLA doesn't install
itself. Here's the no-bullshit guide to get it running on your Omarchy setup
(which is basically Arch with a fancy name, but whatever). Run these commands
one by one, or screw it up and blame yourself.

    sudo pacman -Syu binutils
    sudo pacman -Syu
    sudo pacman -S lib32-glibc
    sudo mkdir -p /usr/hla
    cd /usr/hla
    sudo wget https://www.plantation-productions.com/Webster/HighLevelAsm/HLAv2.16/linux64.hla.tar.gz -O /tmp/linux64.hla.tar.gz
    sudo tar -xzf /tmp/linux64.hla.tar.gz -C /usr/hla --strip-components=2  
    sudo chmod +x /usr/hla/hla /usr/hla/hlaparse
    sudo chmod -R +rx /usr/hla/include /usr/hla/hlalib /usr/hla/hlalibsrc
    sudo chmod -R +r /usr/hla/  
    sudo cp /usr/hla/hla /usr/hla/hlaparse /usr/bin/
    vi ~/.bashrc

In that ~/.bashrc, add this crap:

    export PATH="$PATH:/usr/hla"
    export HLALIB="/usr/hla/hlalib"
    export HLAINC="/usr/hla/include"
    export HLATEMP="/tmp"

Then,

    source ~/.bashrc
    # Confirm installation
    hla

## Getting Started
1. **Clone this crap:**

    git clone https://github.com/yourusername/atutor.git
    cd atutor

2. **Run the damn thing:**

    python main.py

- It'll bitch if `tutorial.hla` is missing (it shouldn't be—check your clone).
- Fires up Vim on a temp copy of the tutor. Edit like a savage: uncomment
commands, screw up lessons, whatever. - Quit Vim (`:q` or `ZZ`, you know the
drill). Your half-assed changes? Stick to the temp file. Original stays
pristine. - No Vim? It'll yell at you to install it, then bail. - Compile
manually: `hla temp.hla && ./temp`. Errors? Fix your shit—welcome to assembly.

3. **Pro Tip:** Virtualenv if you're paranoid (on Omarchy: `python -m venv env
&& source env/bin/activate`). But seriously, just run it—it's idiot-proof.

## What's in the Box?
- `tutorial.hla`: The tutor meat. Lessons on HLA basics like programs,
  includes, variables—stuff that makes you productive instead of a GAS fossil.
- `main.py`: The launcher. Copies `tutorial.hla` to temp, spawns Vim, waits for
  you to quit. No auto-compile—do it yourself, build some spine.

## Why Bother?  Because stock assembly tutorials stop at "mov eax, 0" and leave
you wondering why your code faults harder than a kernel panic. This one teaches
you HLA to *assemble* like a pro without carpal tunnel from raw opcodes.
Battle-tested for code that doesn't crash on Tuesdays. Experiment, or don't—HLA
doesn't care, but your binaries will.

## Credits
- Original HLA: Randall Hyde (bless him for making assembly less masochistic).
- This overhaul: Ryan Gerard Wilson (ryangerardwilson.com) or whoever— if it
  sucks, blame him. If it's gold, thank me for the README.

## License
MIT, or whatever—fork it, break it, just don't sue me when your registers overflow.
