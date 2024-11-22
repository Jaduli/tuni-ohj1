"""
COMP.CS.100 Ohjelmointi 1, syksy 2023
Tekijä: Jade Pitkänen, jade.pitkanen@tuni.fi
Opiskelijanumero: 151842146

Gunman- eli pyssymies-peli, jossa reaktionopeutesi laitetaan testiin.
Aloita peli ja odota "Shoot!"-napin ilmestymistä. Ammu pyssysi ennen
vihollista niin voitat. Yritä kerätä mahdollisimman suuri voittoputki.
"""

minimum_reaction_time = 230
maximum_reaction_time = 500
# Pelissä käytettävät reaktioajat normaalimoodissa. Vapaasti muokattavissa
# tarpeen mukaan. Tavallisesti ihmisen reaktioaika on välillä 200-400 ms.

image_files = ["standstill.gif", "shot.gif", "defeat.gif"]
# Pelissä käytetyt kuvat. Myös muokattavissa, mutta pelissä on mukana
# upea itsetehty kuvitus.

from tkinter import *
from random import randint
from time import time

class Gunman:
    def __init__(self):
        """
        Gunman peliin tarvittavat arvot ja komennot.
        """

        self.__window = Tk()

        self.__window.title("Gunman")

        self.__images = []

        # Peli on kuvitettu image_files listasta löytyvillä kuvilla.
        # Kuvat menevät seuraavassa järjestyksessä:
        # 0 = standstill, 1 = shot, 2 = defeat
        for image in image_files:
            self.__images.append(PhotoImage(file=image))

        # Pelin alkutilanne on standstill
        self.__current_image = Label(image=self.__images[0])

        # Asetetaan pelissä tarvittavat napit
        self.__start_button = Button(self.__window, text="Start",
                                     command=self.start)
        self.__wait_button = Button(self.__window, text="Wait for it...",
                                    command=self.too_early)
        self.__shoot_button = Button(self.__window, text="Shoot!",
                                     command=self.shoot)

        # Asetetaan alussa annetut maksimi- ja minimiarvot reaktioajoille.
        self.__minimum_reaction_time = minimum_reaction_time
        self.__maximum_reaction_time = maximum_reaction_time

        # Assarin työn helpottamiseksi ja kehittyneen käyttöliittymän
        # kriteerin täyttämiseksi pelissä on easy mode, jonka voi laittaa
        # päälle ja pois vapaasti Checkbuttonin avulla.
        self.__easy_mode_toggle = IntVar()
        self.__easy_mode = Checkbutton(self.__window, text="Easy mode",
                                       variable=self.__easy_mode_toggle)

        # Game_info-label kertoo ohjelmassa mitä kullakin hetkellä tapahtuu.
        self.__game_info = Label(self.__window, text="Start the game, "
                                "then wait for the 'Shoot' button to appear.")

        self.__reset_button = Button(self.__window, text="Reset",
                                     command=self.reset_game)

        self.__quit_button = Button(self.__window, text="Quit",
                                    command=self.quit)

        # Pelissä on myös voittoputki-laskuri hauskuuden vuoksi.
        self.__streak_counter = 0
        self.__streak_counter_label = Label(self.__window, text=f"Win streak: "
                                            f"{str(self.__streak_counter)}")

        self.__start_time = 0
        # = ajanhetki, jolloin "Shoot!"-nappi ilmestyy. Lasketaan koodissa
        # Time-komennolla. Käytetään pelaajan reaktioajan laskemiseen.

        self.__reaction_time = Label()
        self.__enemy_reaction_time = Label()

        # Pelin alkuasetelmat:
        self.__current_image.pack()
        self.__game_info.pack()
        self.__start_button.pack()
        self.__quit_button.pack()
        self.__easy_mode.pack(side="left")


    def start(self):
        """
        Aloittaa varsinaisen reaktioaikapelin. Jotta napin painaminen ei olisi
        niin helppoa, se ilmestyy satunnaisella aikavälillä (2s-6s).
        """

        self.__game_info.configure(text="")

        self.__streak_counter_label.pack_forget()
        self.__easy_mode.pack_forget()
        self.__start_button.pack_forget()
        self.__quit_button.pack_forget()

        self.__wait_button.pack()

        # Aloitetaan ajastin
        wait_time = randint(2000, 6000)
        self.__wait_time = self.__window.after(wait_time, self.update_button)

    def update_button(self):
        """
        Jos pelaaja ei painanut nappia liian ajoissa, "Shoot!" nappi ilmestyy
        satunnaisen ajan jälkeen. Tämän jälkeen hänellä on satunnainen aika
        painaa nappia, tai hän häviää vastustajalle.
        """

        # Tarkistetaan, onko easy mode päällä
        self.toggle_easy_mode()

        self.__wait_button.pack_forget()
        self.__shoot_button.pack()

        min_reaction_time = self.__minimum_reaction_time
        max_reaction_time = self.__maximum_reaction_time
        shot_wait_time = randint(min_reaction_time, max_reaction_time)

        self.__start_time = time()

        # Asetetaan vihollisen reaktioaika.
        self.__enemy_reaction_time.configure(text=f"Enemy's reaction time:"
                                                  f" {shot_wait_time}ms")

        # Aloitetaan uusi ajastin "Shoot!" napille
        self.__wait_time = self.__window.after(shot_wait_time, self.defeat)

    def shoot(self):
        """
        Jos pelaaja painoi nappia ajoissa, hän voittaa kierroksen. Voittoputki-
        laskurin arvo nousee. Nyt pelaaja voi myös nähdä reaktioaikansa.
        Voittoruudulle on oma kuvansa.
        """

        # Lopetetaan "Shoot!" napin ajastin
        self.__window.after_cancel(self.__wait_time)

        self.__streak_counter += 1
        self.set_streak()

        # Reaktioaika on aikaero "Shoot!" napin painamisen ja
        # ilmestymisen välillä.
        reaction_time = time() - self.__start_time
        self.__reaction_time.configure(text=f"Your reaction time: "
                                        f"{(reaction_time * 1000):.0f}ms")

        self.__game_info.configure(text="Congratulations! You win!")
        self.__current_image.configure(image=self.__images[1])
        self.__shoot_button.pack_forget()

        self.__game_info.pack()
        self.__reaction_time.pack()
        self.__reset_button.pack()
        self.__quit_button.pack()
        self.__streak_counter_label.pack()

    def defeat(self):
        """
        Jos pelaaja oli liian hidas napin painamisessa, hän häviää. Voittoputki
        palaa nollaan. Vihollisen reaktio-aika on myös näkyvissä. Häviämiselle
        on oma kuvansa.
        """

        self.__current_image.configure(image=self.__images[2])
        self.__game_info.configure(text="Too slow! Try again.")
        self.__streak_counter = 0
        self.set_streak()

        self.__shoot_button.pack_forget()

        self.__enemy_reaction_time.pack()
        self.__reset_button.pack()
        self.__quit_button.pack()

    def too_early(self):
        """
        Jos pelaaja hosuu tai yrittää huijata painamalla nappia liian aikaisin,
        hän häviää.
        """

        # Lopetetaan ajastin
        self.__window.after_cancel(self.__wait_time)

        self.__current_image.configure(image=self.__images[2])
        self.__game_info.configure(text="You tried to shoot too early! "
                                        "Game lost.")
        self.__streak_counter = 0
        self.set_streak()

        self.__shoot_button.pack_forget()
        self.__wait_button.pack_forget()

        self.__reset_button.pack()
        self.__quit_button.pack()

    def toggle_easy_mode(self):
        """
        Easy-mode pidentää huomattavasti vihollisen reaktioaikaa, eli peli on
        helpompi voittaa. Tämä on hyvä, jos ohjelman toimivuutta haluaa
        testata, ja tämän avulla melkeinpä kuka vaan voi voittaa pelin.
        """

        if self.__easy_mode_toggle.get() == 1:
            self.__minimum_reaction_time = 1500
            self.__maximum_reaction_time = 2200

        else:
            self.__minimum_reaction_time = minimum_reaction_time
            self.__maximum_reaction_time = maximum_reaction_time

    def set_streak(self):
        """
        Asettaa voittoputken sen arvon perusteella.
        """
        self.__streak_counter_label.configure(text=f"Win streak: "
                                            f"{str(self.__streak_counter)}")

    def reset_game(self):
        """
        Resetoi pelin alkuasetelmiin, tosin nyt myös voittoputki on näkyvissä.
        """

        self.__game_info.configure(text="Start the game,"
                                " then wait for the 'Shoot' button appear.")
        self.__current_image.configure(image=self.__images[0])

        # Poistetaan ensin napit ja labelit
        self.__quit_button.pack_forget()
        self.__wait_button.pack_forget()
        self.__shoot_button.pack_forget()
        self.__streak_counter_label.pack_forget()
        self.__reset_button.pack_forget()
        self.__enemy_reaction_time.pack_forget()
        self.__reaction_time.pack_forget()

        # Palautetaan alkuasetelmaan oikeassa järjestyksessä
        self.__start_button.pack()
        self.__quit_button.pack()
        self.__streak_counter_label.pack()
        self.__easy_mode.pack(side="left")

    def quit(self):
        """
        Lopettaa pelin.
        """
        self.__window.destroy()

    def start_game(self):
        """
        Käynnistää pelin.
        """
        self.__window.mainloop()


def main():

    game = Gunman()
    game.start_game()


if __name__ == "__main__":
    main()
