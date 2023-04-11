# Import(s)


# Map Class
class Map:
    # Constructor method
    def __init__(self):
        self.map_table = []
        self.tiles_list = []

    # Setters
    # Method: set_tiles_list
    # Purpose: Set the tiles list
    def set_tiles_list(self, tiles_list: list):
        self.tiles_list = tiles_list

    # Method: get_number_color
    # Purpose: Return the color of the number based on the number available in the map file
    def get_number_color(self, number: int):
        # Color table
        colors = {
            0: "black",  # Border
            1: "white",  # Empty (road)
            2: "grey",  # Building
            3: "blue",  # Lake
            4: "green",  # Park
        }

        # Return the color
        return colors[number]

    # Method: convert_to_table
    # Purpose: Convert the map file to a table
    def convert_to_table(self, map_file: str):
        # Open the map file
        with open(map_file, "r") as file:
            # Read the file line by line
            for line in file:
                # Remove the \n at the end of the line
                line = line.replace("\n", "")

                # Split the line into a list of characters
                line = list(line)

                # Convert the characters into integers
                line = [int(character) for character in line]

                # Add the line to the map table
                self.map_table.append(line)

    # Method: convert_to_str
    # Purpose: Convert the map table to a string
    def convert_to_str(self, map_table: list):
        # Variable(s)
        map_str = ""

        # Loop through the map table
        for row in range(len(map_table)):
            for column in range(len(map_table[row])):
                # Add the number to the map string
                map_str += str(map_table[row][column])

            # Add a new line to the map string
            map_str += "\n"

    # Method: get_map_table
    # Purpose: Return the map table
    def get_map_table(self):
        return self.map_table