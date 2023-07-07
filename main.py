import socket
import asyncio

async def scan_port(ip, port, socket):
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    if socket.connect_ex((ip, port)):
        return [False, port]
    else:
        return [True, port]

async def main():
    print("Port checker succesful started!")
    await asyncio.sleep(0.5)
    Adress = input("please write a domain: ")
    ipAdress = socket.gethostbyname(Adress)
    for i in range(81):
        response = await scan_port(ipAdress, i, socket)


if __name__ == "__main__":
    asyncio.run(main())