# fourpiskytools

![4 Pi Sky Logo](4ps_logo_small.png)

This repository contains a handful of examples tying together use of the
[voevent-parse](http://voevent-parse.readthedocs.org/) and 
[Comet](http://comet.transientskp.org/) 
packages, providing a 
quick and easy way to get started sending or receiving
[VOEvents](http://voevent.readthedocs.org/)
with the [4 Pi Sky](http://4pisky.org/voevent)
VOEvent broker (or any other VOEvent broker, for that matter).

The code provided here makes many assumptions about what you want to do,
in order to present a simple interface.
Those with more specific requirements should refer to this package as
a quick example, and then use *voevent-parse* and *Comet* directly
(see also: the [voevent-parse tutorial](https://github.com/timstaley/voevent-parse-tutorial), 
and [pysovo](https://github.com/timstaley/pysovo)).

## Quickstart (Ubuntu)

(For the impatient, who are running **Ubuntu/Debian** and have the virtualenv tool available)

    sudo apt-get install libxml2-dev libxslt-dev
    ./INSTALL.sh && ./RUNME.sh

## Installation (including Mac OSX etc)


You'll need to install some Python packages for these scripts to work.
Working in a 
[virtualenv](http://virtualenv.readthedocs.org/en/latest/virtualenv.html)
is recommended, but not essential.
I also recommend use of
[pip](http://pip.readthedocs.org/en/latest/quickstart.html)
since it allows easy version checking and package uninstallation.

Note that one of the python package dependencies is *lxml*, which
has some prerequisites for compilation that can cause a
standard ``pip install``
to fail, sometimes with confusing errors. So it might be a good idea to try

    pip install lxml
    
and see if that works for you.

On Ubuntu you can satisfy those requirements (so you can ``pip install lxml``) 
by running:

    apt-get install libxml2-dev libxslt-dev

before you attempt to install anything else. For more information
(e.g. for Mac OSX), see the relevant 
[Notes on VOEvent section](http://voevent.readthedocs.org/en/latest/setup.html#background-and-dependencies) 
or consult the 
[LXML docs](http://lxml.de/installation.html#installation).

You can check if LXML is already installed by simply trying 

    import lxml
    
in the python interpreter. 

Next, grab a local copy of the `fourpiskytools` repository:

    git clone https://github.com/timstaley/fourpiskytools.git

Then, ``cd fourpiskytools`` and 

    pip install .
    

Or if you prefer the traditional method:

    python setup.py install 

If you run into problems, try consulting the installation guides for
[voevent-parse](http://voevent-parse.readthedocs.org/en/master/intro.html#installation)
and
[Comet](http://comet.transientskp.org/en/1.2.1/installation.html)
and verify that you can install those packages individually.

# Getting started
## Receiving and processing VOEvents
First, you should verify that you can successfully run the `Comet` command 
line tool. For example, at the command line try:

    twistd -n comet -v --local-ivo=ivo://fpstoolstest/foo#bar --remote=voevent.4pisky.org
    
(For more detail, see http://voevent.readthedocs.org/en/latest/receiving.html
and 
[Comet's own docs](http://comet.readthedocs.org/en/stable/usage/broker.html#broker).)

Next we need to actually do something with
the VOEvents as they are received. The simplest way to do this is to 
write a script that can accept the raw XML via stdin (i.e., so you can 
pipe stuff to it via the command line). 
Comet comes with a ``--cmd``
[option](http://comet.readthedocs.org/en/stable/usage/broker.html#spawning-external-commands)
so you can tell it to run a script of your choice and pipe it the XML contents for every VOEvent received.
We need to write a basic Python script to accept this input, 
test it via the command line, and then run Comet with the right command line 
options.

### Example Python response script
The examples folder contains a couple of basic VOEvent processing scripts
to get you started. First, take a look at 
[process_voevent_from_stdin_1.py](examples/process_voevent_from_stdin_1.py).
This very short script just reads in the data from stdin, parses it as a 
VOEvent object, and prints out a couple of key items of information. 

Let's try it out. There's a sample XML packet in the examples folder, 
[test_packet.xml](examples/test_packet.xml). We can test our processing 
script on this packet by piping it in, using the command line. From 
the examples directory:

    cat test_packet.xml | ./process_voevent_from_stdin_1.py
    
You should see something like:

> At 2015-11-12 13:10:47.278333, received VOEvent with IVORN ivo://voevent.organization.tld/TEST#141113-2118.55_ac97a2b6 

> Authored by ivo://voevent.organization.tld at 2014-11-13T21:18:55

The same text should also be output to a logfile, `script1.log`.

The second script, [process_voevent_from_stdin_2.py](examples/process_voevent_from_stdin_2.py), contains
some slightly more interesting logic, so you can change processing depending what sort of VOEvent packet is received.
As an aside, note that if you're on an Ubuntu system, you can ``pip install pgi`` to get pop-up desktop notifications using the code called from script 2.

### Hooking up Comet and the processing script
The examples folder also contains a shell script that runs Comet and passes VOEvents to a handler script - see 
[listen_for_voevents.sh](examples/listen_for_voevents.sh). 
Note that you won't see the command line output from the called script - you'll 
have to inspect the logfile to see the results from processing any 
incoming VOEvents (and you may have to wait for a VOEvent to be broadcast
via the broker!).

## Sending VOEvents
A full guide is on the To Do list! For now, see [send_alert.py](examples/send_alert.py).


## What's in the repository

A quick contents for people who are already familiar with VOEvent, and 
are just looking to copy-and-paste some code-snippets:

* A function providing a *subprocess* wrapper about *comet-sendvo*, to allow
  publishing of VOEvents from a scripted process.
* A simple (~3 lines) routine for generating unique identifiers to tag your
  VOEvents with.
* A couple of ready-made functions that take a dictionary defining the sender's
  'identity' and provide one-liner methods for composing VOEvent packets.
* A shell script demonstrating how to initialise Comet to receive alerts and
  pass them on to a Python script for processing.
* A basic utility class for generating GTK notifications (desktop alerts
  akin to e.g. the 'new email' pop-up that Thunderbird will generate).


## Feedback

Questions? Issues? Happy to help, either drop a note 
[on the issue tracker](https://github.com/timstaley/fourpiskytools/issues)
or send us an email.

## Acknowledgement
If you make use of these examples in work leading to a publication, we ask
that you cite the underlying packages as detailed 
[here](http://comet.transientskp.org/en/1.2.1/)
and 
[here](http://voevent-parse.readthedocs.org/en/master/intro.html#acknowledgement).
