
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

        export PATH="$PATH:/usr/hla"
        export HLALIB="/usr/hla/hlalib"
        export HLAINC="/usr/hla/include"
        export HLATEMP="/tmp"

    source ~/.bashrc
    # Confirm intallation
    hla



