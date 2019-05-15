# Tor-Multiple-Instances
Launch multiple tor proxy instances, useful with crawlers which needs lots of proxies.

# Generate `torrc` file
In order to generate the `torrc` file, Python 3.6 is required.
Execute `python3 torrc_gen.py` and answer the three questions. When the script has finished, a torrc file should be generated with the name you chose. You can use `ls` command to make sure the script worked.

# Run tor
To run tor, just execute `sh launch_tor.sh <torrc filename here>` specifying the torrc filename you chose as commandline argument. If no errors was reported by tor, it should be started successfully.

# Make sure tor has started
The last file, `check_tor.sh` simply outputs all the opened sockets by tor. You can run it using `sh check_tor.sh` command.

# Notes
This project is not yet production ready. Feel free to open an issue if you encounter any problem.
