def merge_files(file_paths_file, file_names_file, output_file):
    with open(file_paths_file, 'r') as paths_file, open(file_names_file, 'r') as names_file, open(output_file, 'w') as output:
        for path, name in zip(paths_file, names_file):
            path = path.strip()
            name = name.strip()
            output.write(f"{path},{name}\n")

def main():
    file_paths_file = 'file_paths.txt'  # Replace with the actual path of your file containing file paths
    file_names_file = 'file_names.txt'  # Replace with the actual path of your file containing file names
    output_file = 'merged_file.txt'     # Replace with the desired output file name

    merge_files(file_paths_file, file_names_file, output_file)
    print("Files merged successfully.")

if __name__ == "__main__":
    main()
