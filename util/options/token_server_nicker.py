from util import *

def send(nick, guild_id, token):
    session = Client.get_session(token)
    result = session.patch(f"https://discord.com/api/v9/guilds/{guild_id}/members/@me", json={'nick': nick})
    if result.status_code == 200:
        Output("good", token).log(f"Success -> {token} {Fore.LIGHTBLACK_EX}({result.status_code})")
    else:
        Output.error_logger(token, result.text, result.status_code)

def server_nicker():
    Output.set_title(f"Server Nicker")
    guild_id = utility.ask("Guild ID")
    nick = utility.ask("Nick Name")
    max_threads = utility.ask("Thread Count")
    utility.run_threads(max_threads=max_threads, func=send, args=[nick, guild_id])