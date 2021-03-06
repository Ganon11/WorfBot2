import os
import os.path
import time
import logging

# some commands can be executed only if the user's nick is found in this list
owner = list(set([
   'mstark',
   'mstark|home',
   'aletheist',
   'aletheia',
]))

# server to connect to
server = 'card.freenode.net'
# server's port
port = 6667

# bot's nicknames
nicks = list(set(['WorfBot', 'WorfBot2', 'WorfBot3']))
# bot's real name
real_name = 'WorfBot, son of MoghBot'

# channels to join on startup
channels = list(set([
   '#reddit-Christianity',
   '#reddit-OrthodoxChristianity',
   '#mstark',
]))

cmd_char = '!'

cmds = {
   # core commands list, these commands will be run in the same thread as the bot
   # and will have acces to the socket that the bot uses
   'core': list(set([
      'add',
      'channels',
      'join',
      'quit',
   ])),

   # normal commands list, the ones that are accessible to any user
   'user': list(set([
      'about',
      'bible',
      'define',
      'help',
      'heretic',
      'heretics',
      'honor',
      'honour',
      'google',
      'mball',
      'uptime',
      'weather',
      'wiki',
      'xkcd'
   ])),

   # commands list that the bot will execute even if a human didn't request an
   # action
   'auto': list(set([
      'add_heretic',
      'auto_bible',
      'remove_heretic',
   ])),
}

# users should NOT modify below!
log = os.path.join(os.getcwd(), '..', 'logs', '')
logging_level = logging.INFO
start_time = time.time()
current_nick = ''
