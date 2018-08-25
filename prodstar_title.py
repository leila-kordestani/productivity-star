import os


class Introductions:

    def title_marquee(self):
        os.system('clear')
        top_bttm_border = "{:^92}".format("⭐️  "* 16)
        side_border = "{0:14}{1}{0:38}{1}".format(" ", "⭐️  ⭐️")
        print("\n" * 3)
        print(top_bttm_border + "\n" + top_bttm_border)
        print(side_border)
        print("\t\t\b\b\b", "⭐️  ⭐️", "\t\t\b\b\b\b\b\b\b", "\033[1mP R O D U C T I V I T Y\033[0m", "\t\b", "⭐️  ⭐️")
        print("\t\t\b\b\b", "⭐️  ⭐️", "\t\t\t\b\b\b\b\b\b\b\b", "\033[1mS T A R\033[0m", "\t\t\b", "⭐️  ⭐️")
        print(side_border)
        print(top_bttm_border)
        print(top_bttm_border)
        print("\n")

    def menu_select(self):
        print("\t\t\t\t\b\b\b\033[35;5mLET'S GET TO WORK!\033[0m\n") # blinks
        print("\t\t\t\t\b\b\b\b", "1. Start Studying")
        print("\t\t\t\t\b\b\b\b", "2. View Session Stats")
        print("\t\t\t\t\b\b\b\b", "3. Preferences")
        print("\t\t\t\t\b\b\b\b", "4. Help/About Us")
        print("\n" * 1)


#border = "{:^92}".format("⭐️  "* 16)  # more concise version of main border
