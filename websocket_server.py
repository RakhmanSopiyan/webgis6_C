import asyncio
import websockets

async def handler(websocket, path):  # Tambahkan 'path' sebagai argumen kedua
    async for message in websocket:
        print(f"Pesan diterima: {message}")
        await websocket.send(f"Pesan diterima: {message}")

async def main():
    async with websockets.serve(handler, "localhost", 8765):  # Pastikan handler dipanggil dengan dua argumen
        await asyncio.Future()  # Menunggu selamanya

if __name__ == "__main__":
    asyncio.run(main())  # Gunakan asyncio.run() untuk menjalankan event loop
