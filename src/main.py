from textnode import TextNode

def main():
    dummy_node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(dummy_node)
    copy_static()

# Recursive function that copies all the contents of a directory to another directory
def copy_static(original, destination):
    if os.path.exists(original):

        # This checks if the destination path exists. If it doesn't, we make it. If it does, we iterate across it and delete everything in it.
        if not os.path.exists(destination):
            os.mkdir(destination)
        else:
            directory_items = os.listdir(destination)
            for item in directory_items:
                if os.path.isfile(item):
                    os.remove(item)
                else:
                    os.rmtree(item)

        # copy permissions over from the original directory to the new one.
        shutil.copystat(original, destination)

        # create a function we will call recursively to copy over everything
        def helper_function(path, destination):
            current_path = path
            copy_path = destination
            item_list = os.listdir(path)
            for item in item_list:
                if os.path.isfile(item):
                    shutil.copy(item, destination)
                else:
                    next_destination = os.path.join(copy_path, item)
                    os.mkdir(next_destination)
                    next_directory = os.path.join(current_path, item)
                    helper_function(next_directory, next_destination)
                    


        
    else:
        raise Exception("Designated path to copy from does not exist")

if __name__ == "__main__":
    main()