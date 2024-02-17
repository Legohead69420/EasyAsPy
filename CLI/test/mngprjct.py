import argparse
import os
import sys
from colorama import Fore, Back, init
cls = lambda: os.system('cls' if os.name == 'nt' else 'clear')
init()

defaultpath = __file__.replace("CLI\\resources.py", "")
def grabpath(id):
  return defaultpath+f"RESOURCES\\{id}.py"

class Resources:
  def getresource(id) -> str:
    return open(grabpath(id), 'r').read()

def parsermanager(args):
  match args.command:
    case "compile":
      try:
        os.system(f"pyinstaller --onefile {__file__.replace(f'test\\mngprjct.py"', "")}")
      except Exception as e:
        rprint("error", f"Exception: {e}")
    case _:
      rprint("error", "Unknown command")

def grabinfo(args, project="test"):
  print(open("prjctinfo.log", "r").read())

def rprint(mode: str, content):
  cls()
  match mode.lower():
    case "info":
      print(f"{Fore.GREEN}INFO: {Fore.RESET}"+content)
      return
    case "error":
      print(f"{Fore.RED}ERROR: {Fore.RESET}"+content)
      return
    case "fault":
      print(f"{Fore.YELLOW}FAULT: {Fore.RESET}"+content)
      return

def main():
    cls()
    parser = argparse.ArgumentParser(description=f'Your project manager CLI')
    subparsers = parser.add_subparsers()

    manager = subparsers.add_parser('manage', help='Manage your project')
    manager.add_argument("command", help="Command to manage project")
    manager.set_defaults(func=parsermanager)

    info = subparsers.add_parser("info", help="Show info about the project")
    info.set_defaults(func=grabinfo)
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
  main()
