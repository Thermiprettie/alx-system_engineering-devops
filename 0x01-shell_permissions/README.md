This is a readme file for the 0x01-shell permissions folder. This folder contains scripts that does the following:
0. switches the current user to the user betty
1. prints the effective username of the current user
2. prints all the groups the current user is part of
3. changes the owner of the file hello to the user betty
4. creates an empty file called hello
5. adds execute permission to the owner of the file hello in the working directory
6. that adds execute permission to the owner and the group owner, and read permission to other users, to the file hello
7. adds execution permission to the owner, the group owner and the other users, to the file hello
8. sets the permission to the file hello as follows:

- Owner: no permission at all

- Group: no permission at all

- Other users: all the permissions
9. sets the mode of the file hello to -rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello
10. sets the mode of the file hello the same as olleh’s mode
11. adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files should not be changed
12. creates a directory called my_dir with permissions 751 in the working directory
13. changes the group owner to school for the file hello
14. changes the owner to vincent and the group owner to staff for all the files and directories in the working directory
15. changes the owner and the group owner of _hello to vincent and staff respectively
16. changes the owner of the file hello to betty only if it is owned by the user guillaume
17. that will play the StarWars IV episode in the terminal 
