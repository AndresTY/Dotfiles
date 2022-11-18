#
# ~/.bashrc
#
neofetch
# If not running interactively, don't do anything
[[ $- != *i* ]] && return

HISTSIZE= HISTFILESIZE=

PS1='\[\033[38;5;80m\]\W\[$(tput sgr0)\] \[$(tput sgr0)\]\[\033[38;5;6m\]> \[$(tput sgr0)\]'

export GPG_TTY=$(tty)

alias sdn='sudo shutdown now'

#Alias
alias p='sudo pacman'
alias nv='nvim'
alias snv='sudo nvim'
alias nm='nmcli'
alias sys='sudo systemctl'
alias bth='bluetoothctl; pavucontrol'

#Adding Color
alias ls='ls -hN --color=auto --group-directories-first'
alias grep='grep --color=auto'
