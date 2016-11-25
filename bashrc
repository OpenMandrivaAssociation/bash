# /etc/bashrc

# System wide functions and aliases
# Environment stuff goes in /etc/profile

# It's NOT good idea to change this file unless you know what you
# are doing. Much better way is to create custom.sh shell script in
# /etc/profile.d/ to make custom changes to environment. This will
# prevent need for merging in future updates.

# By default, we want this to get set.
# Even for non-interactive, non-login shells.
if [ "`id -gn`" = "`id -un`" -a `id -u` -gt 99 ]; then
    umask 002
else
    umask 022
fi

# are we an interactive shell?
if [ "$PS1" ]; then
    case $TERM in
	xterm*)
	    PROMPT_COMMAND='echo -ne "\033]0;${USER}@${HOSTNAME%%.*}:${PWD/#$HOME/~}"; echo -ne "\007"'
	    PROMPT_COMMAND='printf "\033]0;%s@%s:%s\007" "${USER}" "${HOSTNAME%%.*}" "${PWD/#$HOME/\~}"'
	    ;;
	screen)
	    PROMPT_COMMAND='echo -ne "\033_${USER}@${HOSTNAME%%.*}:${PWD/#$HOME/~}"; echo -ne "\033\\"'
	    ;;
	*)
	    ;;
    esac

# Turn on parallel history
    shopt -s histappend
    history -a
# Turn on checkwinsize
    shopt -s checkwinsize

    [ "$PS1" = "\\s-\\v\\\$ " ] && PS1="[\u@\h \W]\\$ "
# For a more colorful version, use:
# [ "$PS1" = "\\s-\\v\\\$ " ] && PS1="\[\033[38;5;38m\]\H\[$(tput sgr0)\]\[\033[38;5;41m\]@\[$(tput sgr0)\]\[\033[38;5;38m\]\u\[$(tput sgr0)\]\[\033[38;5;249m\]:\[$(tput sgr0)\]\[\033[38;5;245m\][\[$(tput sgr0)\]\[\033[38;5;33m\]\w\[$(tput sgr0)\]\[\033[38;5;245m\]]\[$(tput sgr0)\]\[\033[38;5;15m\] \[$(tput sgr0)\]\[\033[38;5;196m\]\\$\[$(tput sgr0)\]\[\033[38;5;15m\] \[$(tput sgr0)\]"
# You might want to have e.g. tty in prompt (e.g. more virtual machines)
# and console windows
# If you want to do so, just add e.g.
# if [ "$PS1" ]; then
#	PS1="[\u@\h:\l \W]\\$ "
# fi
# to your custom modification shell script in /etc/profile.d/ directory

    if [ -z "$loginsh" ]; then # We're not a login shell
# Not all scripts in profile.d are compatible with other shells
# TODO: make the scripts compatible or check the running shell by
# themselves.
	if [ -n "${BASH_VERSION}${KSH_VERSION}${ZSH_VERSION}" ]; then
	    for i in /etc/profile.d/*.sh; do
		if [ -r $i ]; then
		    . $i
		fi
	    done
	    unset i
	fi
    fi
fi

unset loginsh
