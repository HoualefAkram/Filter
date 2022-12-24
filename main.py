import shutil
import os
from pathlib import Path
import sys

sys.setrecursionlimit(999999)
while True:
    try:
        def trasnlate(directory):
            directory = directory.replace("\\", "/")
            return directory


        main_directory = trasnlate(input("\n\nMain directory: "))
        filter_directory = trasnlate(input("Filter directory: "))

        os.mkdir(filter_directory + "/" + "FILTER")
        Filter_folder = filter_directory + "/" + "FILTER"
        scan = input('do you want to filter folders inside of your folders (yes/no) : ')

        Formats = []
        Formats_fold = []
        random_files = []
        random_folder = Filter_folder + "/" + "Files Without extension"
        os.mkdir(random_folder)

        if scan.lower() == 'no':
            quest = input("(copy/move) : ")

            for files in os.listdir(main_directory):
                main_main = os.path.join(main_directory, files)
                if os.path.isdir(main_main) is True:
                    Formats_fold.append(files)
                if files not in Formats_fold and files not in random_files and Path(files).suffix == '':
                    random_files.append(files)
                if files.split('.')[-1] not in Formats and files not in Formats_fold and Path(
                        files).name not in random_files:
                    Formats.append(files.split('.')[-1])
                    os.mkdir(Filter_folder + "/" + files.split('.')[-1])
                    os.access(main_directory, os.W_OK)
                final_folder = Filter_folder + "/" + files.split('.')[-1]

                if quest.lower() == 'move' and files not in Formats_fold and files not in random_files:
                    shutil.move(f"{main_directory}\\{files}", final_folder)

                elif quest.lower() == 'copy' and files not in Formats_fold and files not in random_files:
                    shutil.copy(f"{main_directory}\\{files}", final_folder)

                if quest.lower() == 'copy' and files not in Formats_fold and files in random_files:
                    os.access(Path(files), os.W_OK)
                    shutil.copy(f"{main_directory}\\{files}", random_folder)
                if quest.lower() == 'move' and files not in Formats_fold and files in random_files:
                    os.access(Path(files), os.W_OK)
                    shutil.move(f"{main_directory}\\{files}", random_folder)

            if quest.lower() != 'copy' and quest.lower() != 'move':
                print('invalid Input , please write copy or move')
                shutil.rmtree(Filter_folder)

            if quest.lower() == 'copy' or quest.lower() == 'move':
                print('    Done !')

        if scan.lower() == "yes":
            quest = input("(copy/move) : ")
            for files in Path(main_directory).glob("**/*"):
                if os.path.isdir(Path(files)):
                    Formats_fold.append(files.name)
                if os.path.isfile(Path(files)) and Path(files).name not in random_files and Path(files).suffix == '':
                    random_files.append(files.name)

                if files.name not in Formats_fold and files.name.split('.')[
                    -1] not in Formats and files.name not in random_files:
                    Formats.append(files.name.split('.')[-1])
                    os.mkdir(Filter_folder + "/" + files.name.split('.')[-1])
                    os.access(main_directory, os.W_OK)
                final_folder = Filter_folder + "/" + files.name.split('.')[-1]
                if quest.lower() == 'copy' and files.name not in Formats_fold and files.name not in random_files:
                    os.access(Path(files), os.W_OK)
                    shutil.copy(Path(files), final_folder)
                if quest.lower() == 'move' and files.name not in Formats_fold and files.name not in random_files:
                    os.access(Path(files), os.W_OK)
                    shutil.move(str(files), str(final_folder))

                if quest.lower() == 'copy' and files.name not in Formats_fold and files.name in random_files:
                    os.access(Path(files), os.W_OK)
                    shutil.copy(str(files), str(random_folder))
                if quest.lower() == 'move' and files.name not in Formats_fold and files.name in random_files:
                    os.access(Path(files), os.W_OK)
                    shutil.move(str(files), str(random_folder))

            if quest.lower() != 'copy' and quest.lower() != 'move':
                print('invalid Input , please write copy or move')
                shutil.rmtree(Filter_folder)

            if quest.lower() == 'copy' or quest.lower() == 'move':
                print('    Done !')

        if scan.lower() not in ["no", "yes"]:
            print('Invalid answer, Write \'Yes\' or \'no\'.')
            shutil.rmtree(Filter_folder)

        if not random_files:
            shutil.rmtree(random_folder)


    except FileNotFoundError as err:
        print(err)
    except FileExistsError as err2:
        print(err2)
