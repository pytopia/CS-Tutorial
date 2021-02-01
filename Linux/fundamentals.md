# Linux Fundamentals
One of the biggest reasons for someone to switch to Linux is to use what is arguably the most powerful feature of the Linux operating system and that is the terminal.

Now if you've ever seen a film where a hacker or a computer genius has sat behind their computer typing commands into what looks like a big black box on their computer screen that black box is called the **terminal**.

Now Linux is unique in that the development of Linux is inseparable from the terminal and this means that knowing how to use the terminal gives you pretty much absolute control over how your computer works by using the terminal. You can do pretty much anything that you want with your Linux computer.

Now you can't get this level of control over your computer in any other operating system and this makes the terminal an incredible skill to learn.

**Note:** Don't worry about memorizing all the commands.

## Windows Subsystem for Linux (WSL) Settings
If you are using WSL:
1. Right click in the top title bar of the terminal window (this is the likely gray part of the window with an orange circle on the left).
2. From the menu that appears upon right click, select properties.
3. Select Font, and choose the size you’d like (I prefer size 20 for my WSL windows)
4. Then select OK (once OK is clicked the windows and the window text should resize to the selected font size).

**Recommended changes**:
- In Options tab:
  - Check `Use Ctrl+Shift+C/V as Copy/Pase`
- In Font tab:  
  - Font size: 36
- In Layout tab:
  - Width: 80
  - Height: 18
- In Terminal tab:
  - Check `Disable Scroll-Forward`

## Directories
### Common Directories
- `/`: root
  - `/bin`: binary or other executalbe programs
  - `/etc`: system configuration files
  - `/home`: home directories
    - `user_name`
      - Documents
      - Downloads
      - Music
      - ...
  - `/opt`: optional or third party softwares
  - `/tmp`: temporary space, typically cleared on reboot
  - `/usr`: user related programs
  - `/var`: variable data, most notably log files
    - `log`
  - `/boot`: files needed to boot the operating system
  - `/cdrom`: mount point for CD-ROMs
  - `/dev`: device files, typically controlled by the operating system and the system administrators.
  - `/lib`: system libraries
  - `/lib64`: system libraries, 64 bit
  - `/lost+found`: Used by the file system to store recovered files after a file system check has been performed.
  - `/media`: Used to mount removable media like CD-ROMs
  - `/mnt`: used to mount external file systems.

### Application Directory Structures
- `/usr/local/application/bin`
- `/usr/local/application/etc`
- `/usr/local/application/lib`
- `/usr/local/application/log`

- `/opt/application/bin`
- `/opt/application/etc`
- `/opt/application/lib`
- `/opt/application/log`

Applications that are not part of the base OS can be installed in:
- `/usr/local`
- `/opt`

## Basic Linux Commands

- Print "Hello World": `echo Hello World`
- Calendar: `cal`, `cal 2021`, `cal -y`
- Today date: `date`
- Clear Screen: `ctrl + L`

You can keep pressing up and cycling backwards through the commands that you've already run which is very very useful.

You can also look at your whole command history using what's called the history command, so if you type history and press ENTER we can see all of our previous commands with the line number associated with them.

To run a line number in history again, instead of having to cycle all the way back up to number 1, what I could do is look a tide the exclamation mark and then 1. For example:
- `!1`: Running the first command in history.
- `!275`: Runnign the 275th command in history.

To run the most recent command: `!!`
To exit the terminal: `exit`

- `ls`
  - `ls -l`: `-rw-rw-r-- 1 jason users 10400 Sep 27 08:52 sales.data`
    - `-rw-rw-r--`: permissions
    - 1: number of links
    - `jason`: owner name
    - `users`: group name
    - 10400: number of bytes in the file
    - Sep 27 08:52: last modification time
    - sales.data: file name
  - `ls -a`: listing all files including hidden files
    - hiden files begin with a period (`.git` for example)
  - `ls -F`: listing files by type
    - `/`: Directory
    - `@`: Link
    - `*`: Executable
  - `ls -t`: list files by time
  - `ls -r`: reverse order
  - `ls -l -a` or `ls -la` or `ls -al`: combine options
- `tree`: similar to `ls`, but creates visual output
  - `tree -d`: list directories only
- `cd`
- `pwd`
- `cat`: concatenates and displays files
- `echo`: displays arguments to the screen
- `man`: displays the online manual
  - `man -k SEARCH_TERM`: searching man pages
- `exit`: exits the shell or your current session
- `clear`: clears the screen
- `reset`: resets the shell or your current session
- `which`: locate a command
- `groups`: displays a user's groups
