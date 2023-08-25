
import asyncio
import bleak  # Bleak is a GATT client for use with BLE devices.

# MAC address of the Fitbit Sense (masked for privacy reasons)
fitbit_mac_address = "xx:xx:xx:xx:xx:xx"

# Sample data to be sent to the Fitbit Sense. This is a repetition of the alphabet to demonstrate a long message.
large_data = b"ABCDEFGHIJKLMNOPQRSTUVWXYZ" * 10000

# The size of each chunk in which the large data will be divided for transmission
chunk_size = 2

# Time to wait between sending each chunk (in seconds)
delay_between_packets = 0

async def main():
    # Connect to the Fitbit Sense device using its MAC address
    async with bleak.BleakClient(fitbit_mac_address) as client:
        print("Connected to Fitbit Sense!")

        # UUID of the characteristic we want to write to on the Fitbit Sense
        target_characteristic_uuid = "ac2f0a45-8182-4be5-91e0-2992e6b40ebb"
        target_characteristic = None
        
        # Search for the target characteristic on the device
        for service in await client.get_services():
            for characteristic in service.characteristics:
                if characteristic.uuid == target_characteristic_uuid and "write" in characteristic.properties:
                    target_characteristic = characteristic
                    break
            if target_characteristic:
                break

        # If we couldn't find the target characteristic or it doesn't support writing, exit
        if not target_characteristic:
            print("Target characteristic not found or does not support write operation.")
            return

        try:
            while True:
                # Split the large data into chunks based on the defined chunk_size and send them one by one
                for i in range(0, len(large_data), chunk_size):
                    chunk = large_data[i : i + chunk_size]
                    try:
                        # Write the chunk of data to the characteristic on the Fitbit Sense
                        await client.write_gatt_char(target_characteristic.uuid, chunk, response=True)
                        print(f"Data chunk sent to Fitbit Sense on Characteristic: {target_characteristic.uuid}")
                    except bleak.exc.BleakError:
                        print(f"Failed to send data chunk to Characteristic: {target_characteristic.uuid}")

                    # Pause for a short time between chunks to avoid overloading the Fitbit Sense
                    await asyncio.sleep(0)  

                # Wait for the defined delay_between_packets before sending the next set of chunks
                await asyncio.sleep(delay_between_packets)

        except KeyboardInterrupt:
            # If the user interrupts the loop (e.g. using Ctrl+C), stop the program
            print("Loop interrupted by user (Ctrl+C). Stopping...")

# If the script is executed directly, run the main function
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
