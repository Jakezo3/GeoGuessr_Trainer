import tkinter as tk
from tkinter import messagebox, simpledialog

class CountryDeterminer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Country Determiner")
        self.geometry("550x750")

        # Initial list of all countries
        initial = [
            'Albania','Andorra','Argentina','Australia','Austria','Bangladesh','Belgium','Bhutan',
            'Bolivia','Botswana','Brazil','Bulgaria','Cambodia','Canada','Chile','Colombia','Croatia',
            'Czechia','Denmark','Dominican_Republic','Ecuador','Estonia','Eswatini','Finland','France',
            'Germany','Ghana','Greece','Greenland','Guatemala','Hungary','Iceland','Indonesia','Ireland',
            'Israel','Italy','Japan','Jordan','Kenya','Kyrgyzstan','Latvia','Lesotho','Lithuania',
            'Luxembourg','Malaysia','Mexico','Mongolia','Montenegro','Netherlands','New_Zealand','Nigeria',
            'North_Macedonia','Norway','Panama','Peru','Philippines','Poland','Portugal','Romania','Russia',
            'Senegal','Serbia','Singapore','Slovakia','Slovenia','South_Africa','South_Korea','Spain',
            'Sri_Lanka','Sweden','Switzerland','Taiwan','Thailand','Turkey','Ukraine','United_Arab_Emirates',
            'United_Kingdom','United_States','Uruguay','Vietnam','Venuzela'
        ]
        # Preserve original full list for resets
        self.initial_countries = initial.copy()
        self.countries = initial.copy()

        # Listbox for remaining countries
        self.listbox = tk.Listbox(self, height=20, width=60)
        self.listbox.pack(padx=10, pady=10)
        scrollbar = tk.Scrollbar(self, command=self.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=scrollbar.set)
        self.update_listbox()
        
        

        # Frame for input fields
        entry_frame = tk.LabelFrame(self, text="Enter Your Observations", padx=10, pady=10)
        entry_frame.pack(fill=tk.X, padx=10, pady=5)

        # Driving side
        tk.Label(entry_frame, text="Driving side (left/right):").grid(row=0, column=0, sticky=tk.W)
        self.driving_var = tk.StringVar()
        drv_entry = tk.Entry(entry_frame, textvariable=self.driving_var)
        drv_entry.grid(row=0, column=1, sticky=tk.W)

        # Zebra crossings
        tk.Label(entry_frame, text="Zebra crossings? (yes/no):").grid(row=1, column=0, sticky=tk.W)
        self.zebra_var = tk.StringVar()
        zebra_entry = tk.Entry(entry_frame, textvariable=self.zebra_var)
        zebra_entry.grid(row=1, column=1, sticky=tk.W)
        tk.Label(entry_frame, text="Number seen:").grid(row=2, column=0, sticky=tk.W)
        self.zebra_amt_var = tk.StringVar()
        zebra_amt_entry = tk.Entry(entry_frame, textvariable=self.zebra_amt_var)
        zebra_amt_entry.grid(row=2, column=1, sticky=tk.W)

        # Sun position
        tk.Label(entry_frame, text="Sun position (north/south):").grid(row=3, column=0, sticky=tk.W)
        self.sun_var = tk.StringVar()
        sun_entry = tk.Entry(entry_frame, textvariable=self.sun_var)
        sun_entry.grid(row=3, column=1, sticky=tk.W)

        # URL ending
        tk.Label(entry_frame, text="URL ending present? (yes/no):").grid(row=4, column=0, sticky=tk.W)
        self.url_pres_var = tk.StringVar()
        url_pres_entry = tk.Entry(entry_frame, textvariable=self.url_pres_var)
        url_pres_entry.grid(row=4, column=1, sticky=tk.W)
        tk.Label(entry_frame, text="URL ending:").grid(row=5, column=0, sticky=tk.W)
        self.url_end_var = tk.StringVar()
        url_end_entry = tk.Entry(entry_frame, textvariable=self.url_end_var)
        url_end_entry.grid(row=5, column=1, sticky=tk.W)

        # Stop sign
        tk.Label(entry_frame, text="Stop sign present? (yes/no):").grid(row=6, column=0, sticky=tk.W)
        self.stop_var = tk.StringVar()
        stop_entry = tk.Entry(entry_frame, textvariable=self.stop_var)
        stop_entry.grid(row=6, column=1, sticky=tk.W)
        tk.Label(entry_frame, text="Stop sign text:").grid(row=7, column=0, sticky=tk.W)
        self.stop_lang_var = tk.StringVar()
        stop_lang_entry = tk.Entry(entry_frame, textvariable=self.stop_lang_var)
        stop_lang_entry.grid(row=7, column=1, sticky=tk.W)

        # License plate
        tk.Label(entry_frame, text="License plate color:").grid(row=8, column=0, sticky=tk.W)
        self.plate_var = tk.StringVar()
        plate_entry = tk.Entry(entry_frame, textvariable=self.plate_var)
        plate_entry.grid(row=8, column=1, sticky=tk.W)

        # Writing system
        tk.Label(entry_frame, text="Writing seen? (yes/no):").grid(row=9, column=0, sticky=tk.W)
        self.write_var = tk.StringVar()
        write_entry = tk.Entry(entry_frame, textvariable=self.write_var)
        write_entry.grid(row=9, column=1, sticky=tk.W)
        tk.Label(entry_frame, text="Writing language:").grid(row=10, column=0, sticky=tk.W)
        self.write_lang_var = tk.StringVar()
        write_lang_entry = tk.Entry(entry_frame, textvariable=self.write_lang_var)
        write_lang_entry.grid(row=10, column=1, sticky=tk.W)

        # Trace changes to auto-apply filters
        for var in [self.driving_var, self.zebra_var, self.zebra_amt_var,
                    self.sun_var, self.url_pres_var, self.url_end_var,
                    self.stop_var, self.stop_lang_var, self.plate_var,
                    self.write_var, self.write_lang_var]:
            var.trace_add('write', lambda *args: self.apply_filters())

        # Button to reset
        tk.Button(self, text="Reset", command=self.reset_filters).pack(pady=10)

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for c in self.countries:
            self.listbox.insert(tk.END, c)
        self.update_idletasks()

    def check_single(self):
        if len(self.countries) == 1:
            messagebox.showinfo("Country Found", f"The country is: {self.countries[0]}", parent=self)
            return True
        return False

    def show_result(self):
        if not self.countries:
            msg = "No countries match your criteria."
        else:
            pass
            msg = f"Possible countries:\n{', '.join(self.countries)}"
        messagebox.showinfo("Result", msg, parent=self)

    def apply_filters(self):
        # Start fresh each time so answers can be changed
        self.countries = self.initial_countries.copy()

        # Driving
        side = self.driving_var.get().strip().lower()
        if side in ("left","right"): self.filter_by_driving(side)
        if self.check_single(): return

        # Zebra
        zebra = self.zebra_var.get().strip().lower()
        if zebra == "yes":
            self.filter_by_zebra_yes()
            amt = self.zebra_amt_var.get().strip()
            if amt.isdigit(): self.filter_by_zebra_amount(int(amt))
        elif zebra == "no":
            self.filter_by_no_zebra()
        if self.check_single(): return

        # Sun
        sun = self.sun_var.get().strip().lower()
        if sun in ("north","south"): self.filter_by_sun(sun)
        if self.check_single(): return

        # URL
        up = self.url_pres_var.get().strip().lower()
        if up == "yes":
            ending = self.url_end_var.get().strip().lower()
            if ending: self.filter_by_url(ending)
        if self.check_single(): return

        # Stop
        st = self.stop_var.get().strip().lower()
        if st == "yes":
            lang = self.stop_lang_var.get().strip().lower()
            if lang: self.filter_by_stop(lang)
        if self.check_single(): return

        # Plate
        pl = self.plate_var.get().strip().lower()
        if pl: self.filter_by_license_plate(pl)
        if self.check_single(): return

        # Writing
        wr = self.write_var.get().strip().lower()
        if wr == "yes":
            wl = self.write_lang_var.get().strip().lower()
            if wl: self.filter_by_writing(wl)
        if self.check_single(): return

        self.update_listbox()

    def reset_filters(self):
        # Restore original country list and clear inputs
        self.countries = self.initial_countries.copy()
        self.update_listbox()
        # Clear all input fields
        for var in [self.driving_var, self.zebra_var, self.zebra_amt_var,
                    self.sun_var, self.url_pres_var, self.url_end_var,
                    self.stop_var, self.stop_lang_var, self.plate_var,
                    self.write_var, self.write_lang_var]:
            var.set("")

    # ask_ methods remain the same dialogs calling filter_ methods
    def ask_driving(self):
        side = simpledialog.askstring("Driving Side", "Which side of the road do you drive on? (left/right)", parent=self)
        if side:
            self.filter_by_driving(side.strip().lower())

    def ask_zebra(self):
        zebra = simpledialog.askstring("Zebra Crossings", "Do you have zebra crossings? (yes/no)", parent=self)
        if zebra and zebra.strip().lower() == "yes":
            self.filter_by_zebra_yes()
            amt = simpledialog.askinteger("Zebra Count", "How many zebra crossings have you seen?", parent=self)
            if amt is not None:
                self.filter_by_zebra_amount(amt)
        else:
            self.filter_by_no_zebra()

    def ask_sun(self):
        sun = simpledialog.askstring("Sun Position", "Where is the sun in the sky? (north/south)", parent=self)
        if sun:
            self.filter_by_sun(sun.strip().lower())

    def ask_url(self):
        url_yes = simpledialog.askstring("URL Present", "Do you see a URL ending? (yes/no)", parent=self)
        if url_yes and url_yes.strip().lower() == "yes":
            ending = simpledialog.askstring("URL Ending", "What is the URL ending?", parent=self)
            if ending:
                self.filter_by_url(ending.strip().lower())

    def ask_stop(self):
        stop = simpledialog.askstring("Stop Sign", "Do you see a stop sign? (yes/no)", parent=self)
        if stop and stop.strip().lower() == "yes":
            lang = simpledialog.askstring("Stop Sign Language", "What does the stop sign say? (stop/pare/alto/dur)", parent=self)
            if lang:
                self.filter_by_stop(lang.strip().lower())

    def ask_plate(self):
        lp = simpledialog.askstring("License Plate", "What color is the license plate? (yellow/1blue/2blue/other/none)", parent=self)
        if lp:
            self.filter_by_license_plate(lp.strip().lower())

    def ask_writing(self):
        writing = simpledialog.askstring("Writing", "Do you see writing? (yes/no)", parent=self)
        if writing and writing.strip().lower() == "yes":
            lang = simpledialog.askstring("Language", "Language of writing? (english/european/cyrilic/spanish/characters)", parent=self)
            if lang:
                self.filter_by_writing(lang.strip().lower())


    def filter_by_driving(self, side):
        left_remove = [
            'Albania', 'Andorra', 'Argentina', 'Austria', 'Belgium', 'Bolivia', 'Brazil', 'Bulgaria', 'Cambodia',
            'Canada', 'Chile', 'Colombia', 'Croatia', 'Czechia', 'Denmark', 'Dominican_Republic', 'Ecuador', 'Estonia',
            'Finland', 'France', 'Germany', 'Ghana', 'Greece', 'Greenland', 'Guatemala', 'Hungary', 'Iceland', 'Israel',
            'Italy', 'Jordan', 'Kyrgyzstan', 'Latvia', 'Lithuania', 'Luxembourg', 'Mexico', 'Mongolia', 'Montenegro',
            'Netherlands', 'Nigeria', 'North_Macedonia', 'Norway', 'Panama', 'Peru', 'Philippines', 'Poland', 'Portugal',
            'Romania', 'Russia', 'Senegal', 'Serbia', 'Slovakia', 'Slovenia', 'South_Korea', 'Spain', 'Sweden', 'Switzerland',
            'Taiwan', 'Turkey', 'Ukraine', 'United_Arab_Emirates', 'United_States', 'Uruguay', 'Vietnam', 'Venuzela'
        ]
        right_remove = [
            'Australia', 'Bangladesh', 'Bhutan', 'Botswana', 'Eswatini', 'Indonesia', 'Ireland', 'Japan', 'Kenya',
            'Lesotho', 'Malaysia', 'New_Zealand', 'Singapore', 'South_Africa', 'Sri_Lanka', 'Thailand', 'United_Kingdom'
        ]
        to_remove = left_remove if side == "left" else right_remove
        self.countries = [c for c in self.countries if c not in to_remove]

    def filter_by_zebra_yes(self):
        remove = [
            'Argentina', 'Australia', 'Bangladesh', 'Bhutan', 'Bolivia', 'Botswana', 'Brazil', 'Cambodia', 'Canada',
            'Chile', 'Colombia', 'Dominican_Republic', 'Ecuador', 'Eswatini', 'Ghana', 'Greenland', 'Guatemala',
            'Indonesia', 'Israel', 'Japan', 'Jordan', 'Kenya', 'Kyrgyzstan', 'Lesotho', 'Malaysia', 'Mexico',
            'Mongolia', 'New_Zealand', 'Nigeria', 'Panama', 'Peru', 'Philippines', 'Senegal', 'Singapore',
            'South_Africa', 'South_Korea', 'Sri_Lanka', 'Taiwan', 'Thailand', 'United_Arab_Emirates',
            'United_States', 'Uruguay', 'Vietnam', 'Venuzela'
        ]
        self.countries = [c for c in self.countries if c not in remove]

    def filter_by_zebra_amount(self, amt):
        if amt <= 2:
            remove = [
                'Estonia', 'Latvia', 'Lithuania', 'Russia', 'Ukraine', 'Albania', 'Austria', 'Bulgaria', 'Croatia',
                'Czechia', 'Hungary', 'Italy', 'Montenegro', 'North Macedonia', 'Norway', 'Romania', 'Serbia',
                'Slovakia', 'Slovenia', 'Sweden', 'Andorra', 'Belgium', 'France', 'Germany', 'Iceland',
                'Luxembourg', 'Netherlands', 'Portugal', 'Finland', 'Switzerland', 'Spain'
            ]
        elif amt == 3:
            remove = [
                'Denmark', 'Ireland', 'United Kingdom', 'Greece', 'Turkey', 'Poland', 'Albania', 'Austria',
                'Bulgaria', 'Croatia', 'Czechia', 'Hungary', 'Italy', 'Montenegro', 'North Macedonia', 'Norway',
                'Romania', 'Serbia', 'Slovakia', 'Slovenia', 'Sweden', 'Andorra', 'Belgium', 'France', 'Germany',
                'Iceland', 'Luxembourg', 'Netherlands', 'Portugal', 'Finland', 'Switzerland', 'Spain'
            ]
        elif amt == 4:
            remove = [
                'Denmark', 'Ireland', 'United Kingdom', 'Greece', 'Turkey', 'Poland', 'Estonia', 'Latvia',
                'Lithuania', 'Russia', 'Ukraine', 'Andorra', 'Belgium', 'France', 'Germany', 'Iceland',
                'Luxembourg', 'Netherlands', 'Portugal', 'Finland', 'Switzerland', 'Spain'
            ]
        elif amt == 5:
            remove = [
                'Denmark', 'Ireland', 'United Kingdom', 'Greece', 'Turkey', 'Poland', 'Estonia', 'Latvia',
                'Lithuania', 'Russia', 'Ukraine', 'Albania', 'Austria', 'Bulgaria', 'Croatia', 'Czechia',
                'Hungary', 'Italy', 'Montenegro', 'North Macedonia', 'Norway', 'Romania', 'Serbia',
                'Slovakia', 'Slovenia', 'Sweden', 'Spain'
            ]
        else:
            remove = [
                'Denmark', 'Ireland', 'United Kingdom', 'Greece', 'Turkey', 'Poland', 'Estonia', 'Latvia',
                'Lithuania', 'Russia', 'Ukraine', 'Albania', 'Austria', 'Bulgaria', 'Croatia', 'Czechia',
                'Hungary', 'Italy', 'Montenegro', 'North Macedonia', 'Norway', 'Romania', 'Serbia',
                'Slovakia', 'Slovenia', 'Sweden', 'Andorra', 'Belgium', 'France', 'Germany', 'Iceland',
                'Luxembourg', 'Netherlands', 'Portugal', 'Finland', 'Switzerland', 'Spain'
            ]
        self.countries = [c for c in self.countries if c not in remove]

    def filter_by_no_zebra(self):
        remove = [
            'Albania', 'Andorra', 'Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Czechia', 'Denmark',
            'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy',
            'Latvia', 'Lithuania', 'Luxembourg', 'Montenegro', 'Netherlands', 'North_Macedonia', 'Norway',
            'Poland', 'Portugal', 'Romania', 'Russia', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden',
            'Switzerland', 'Turkey', 'Ukraine', 'United_Kingdom'
        ]
        self.countries = [c for c in self.countries if c not in remove]

    def filter_by_sun(self, pos):
        if pos == "north":
            remove = [
                'Albania', 'Andorra', 'Austria', 'Bangladesh', 'Belgium', 'Bhutan',
    'Bulgaria', 'Cambodia', 'Canada', 'Colombia', 'Croatia', 'Czechia',
    'Denmark', 'Dominican_Republic', 'Estonia', 'Finland', 'France',
    'Germany', 'Ghana', 'Greece', 'Greenland', 'Guatemala', 'Hungary',
    'Iceland', 'Ireland', 'Israel', 'Italy', 'Japan', 'Jordan',
    'Kyrgyzstan', 'Latvia', 'Lithuania', 'Luxembourg', 'Malaysia',
    'Mexico', 'Mongolia', 'Montenegro', 'Netherlands', 'Nigeria',
    'North_Macedonia', 'Norway', 'Panama', 'Philippines', 'Poland',
    'Portugal'
            ]
        if pos == "south":
            remove = [
                'Argentina', 'Australia', 'Bolivia', 'Botswana', 'Brazil', 'Chile',
    'Ecuador', 'Eswatini', 'Indonesia', 'Kenya', 'Lesotho', 'New_Zealand',
    'Peru'
            ]
        self.countries = [c for c in self.countries if c not in remove]

    def filter_by_url(self, ending):
        tlds = {
            'Albania':'al','Andorra':'ad','Argentina':'ar','Australia':'au','Austria':'at','Bangladesh':'bd',
            'Belgium':'be','Bhutan':'bt','Bolivia':'bo','Botswana':'bw','Brazil':'br','Bulgaria':'bg',
            'Cambodia':'kh','Canada':'ca','Chile':'cl','Colombia':'co','Croatia':'hr','Czechia':'cz',
            'Denmark':'dk','Dominican_Republic':'do','Ecuador':'ec','Estonia':'ee','Eswatini':'sz','Finland':'fi',
            'France':'fr','Germany':'de','Ghana':'gh','Greece':'gr','Greenland':'gl','Guatemala':'gt',
            'Hungary':'hu','Iceland':'is','Indonesia':'id','Ireland':'ie','Israel':'il','Italy':'it','Japan':'jp',
            'Jordan':'jo','Kenya':'ke','Kyrgyzstan':'kg','Latvia':'lv','Lesotho':'ls','Lithuania':'lt','Luxembourg':'lu',
            'Malaysia':'my','Mexico':'mx','Mongolia':'mn','Montenegro':'me','Netherlands':'nl','New_Zealand':'nz',
            'Nigeria':'ng','North_Macedonia':'mk','Norway':'no','Panama':'pa','Peru':'pe','Philippines':'ph','Poland':'pl',
            'Portugal':'pt','Romania':'ro','Russia':'ru','Senegal':'sn','Serbia':'rs','Singapore':'sg','Slovakia':'sk',
            'Slovenia':'si','South_Africa':'za','South_Korea':'kr','Spain':'es','Sri_Lanka':'lk','Sweden':'se','Switzerland':'ch',
            'Taiwan':'tw','Thailand':'th','Turkey':'tr','Ukraine':'ua','United_Arab_Emirates':'ae','United_Kingdom':'uk',
            'United_States':'us','Uruguay':'uy','Vietnam':'vn','Venuzela':'ve'
        }
        for name, tld in tlds.items():
            if tld == ending:
                self.countries = [name]
                return
        # no match
        self.countries = []

    def filter_by_stop(self, lang):
        if lang == "stop":
            remove = [
                'Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Peru', 'Uruguay',
                'Venuzela', 'Guatemala', 'Panama', 'Turkey', 'Cambodia', 'Indonesia', 'Malaysia',
                'Philippines', 'Singapore', 'Thailand', 'Vietnam', 'Taiwan', 'Japan', 'Mexico', 'South_Korea'
            ]
        elif lang == "pare":
            remove = [
                'Australia', 'Austria', 'Bangladesh', 'Belgium', 'Bhutan', 'Botswana', 'Bulgaria', 'Canada',
                'Croatia', 'Czechia', 'Denmark', 'Dominican_Republic', 'Estonia', 'Eswatini', 'Finland',
                'France', 'Germany', 'Ghana', 'Greece', 'Greenland', 'Hungary', 'Iceland', 'Ireland',
                'Israel', 'Italy', 'Jordan', 'Kenya', 'Kyrgyzstan', 'Latvia', 'Lesotho', 'Lithuania',
                'Luxembourg', 'Malaysia', 'Mongolia', 'Montenegro', 'Netherlands', 'New_Zealand', 'Nigeria',
                'North_Macedonia', 'Norway', 'Panama', 'Philippines', 'Poland', 'Portugal', 'Romania',
                'Russia', 'Senegal', 'Serbia', 'Singapore', 'Slovakia', 'Slovenia', 'South_Africa',
                'South_Korea', 'Spain', 'Sri_Lanka', 'Sweden', 'Switzerland', 'Taiwan', 'Thailand',
                'Turkey', 'Ukraine', 'United_Arab_Emirates', 'United_Kingdom', 'United_States', 'Vietnam']
            
        elif lang == "alto":
            remove = [
                'Albania', 'Andorra', 'Argentina', 'Australia', 'Austria', 'Bangladesh', 'Belgium', 'Bhutan',
                'Bolivia', 'Botswana', 'Brazil', 'Bulgaria', 'Cambodia', 'Canada', 'Chile', 'Colombia',
                'Croatia', 'Czechia', 'Denmark', 'Dominican_Republic', 'Ecuador', 'Estonia', 'Eswatini',
                'Finland', 'France', 'Germany', 'Ghana', 'Greece', 'Greenland', 'Hungary', 'Iceland',
                'Indonesia', 'Ireland', 'Israel', 'Italy', 'Japan', 'Jordan', 'Kenya', 'Kyrgyzstan',
                'Latvia', 'Lesotho', 'Lithuania', 'Luxembourg', 'Malaysia', 'Mongolia', 'Montenegro',
                'Netherlands', 'New_Zealand', 'Nigeria', 'North_Macedonia', 'Norway', 'Panama', 'Peru',
                'Philippines', 'Poland', 'Portugal', 'Romania', 'Russia', 'Senegal', 'Serbia', 'Singapore',
                'Slovakia', 'Slovenia', 'South_Africa', 'South_Korea', 'Spain', 'Sri_Lanka', 'Sweden',
                'Switzerland', 'Taiwan', 'Thailand', 'Turkey', 'Ukraine', 'United_Arab_Emirates',
                'United_Kingdom', 'United_States', 'Uruguay', 'Vietnam', 'Venuzela'
            ]
        elif  lang ==  "dur":
            remove = [
                'Albania', 'Andorra', 'Argentina', 'Australia', 'Austria', 'Bangladesh', 'Belgium', 'Bhutan',
                'Bolivia', 'Botswana', 'Brazil', 'Bulgaria', 'Cambodia', 'Canada', 'Chile', 'Colombia',
                'Croatia', 'Czechia', 'Denmark', 'Dominican_Republic', 'Ecuador', 'Estonia', 'Eswatini',
                'Finland', 'France', 'Germany', 'Ghana', 'Greece', 'Greenland', 'Guatemala', 'Hungary',
                'Iceland', 'Indonesia', 'Ireland', 'Israel', 'Italy', 'Japan', 'Jordan', 'Kenya', 'Kyrgyzstan',
                'Latvia', 'Lesotho', 'Lithuania', 'Luxembourg', 'Malaysia', 'Mexico', 'Mongolia', 'Montenegro',
                'Netherlands', 'New_Zealand', 'Nigeria', 'North_Macedonia', 'Norway', 'Panama', 'Peru',
                'Philippines', 'Poland', 'Portugal', 'Romania', 'Russia', 'Senegal', 'Serbia', 'Singapore',
                'Slovakia', 'Slovenia', 'South_Africa', 'South_Korea', 'Spain', 'Sri_Lanka', 'Sweden',
                'Switzerland', 'Taiwan', 'Thailand', 'Ukraine', 'United_Arab_Emirates', 'United_Kingdom',
                'United_States', 'Uruguay', 'Vietnam', 'Venuzela'
            ]
        else:
            remove = []

            
        self.countries = [c for c in self.countries if c not in remove]

    def filter_by_license_plate(self, lp):
        remove = []  # Initialize remove to avoid UnboundLocalError
        if lp == "yellow":
            remove = [
                'Albania', 'Andorra', 'Argentina', 'Australia', 'Austria', 'Bangladesh', 'Belgium', 'Bhutan',
                'Bolivia', 'Botswana', 'Brazil', 'Bulgaria', 'Cambodia', 'Canada', 'Chile', 'Croatia',
                'Czechia', 'Dominican_Republic', 'Ecuador', 'Estonia', 'Eswatini', 'Finland', 'France',
                'Germany', 'Ghana', 'Greece', 'Greenland', 'Guatemala', 'Hungary', 'Iceland', 'Indonesia',
                'Ireland', 'Israel', 'Italy', 'Jordan', 'Kenya', 'Kyrgyzstan', 'Latvia', 'Lesotho',
                'Lithuania', 'Malaysia', 'Mexico', 'Mongolia', 'Montenegro', 'New_Zealand', 'Nigeria',
                'North_Macedonia', 'Norway', 'Panama', 'Peru', 'Philippines', 'Poland', 'Portugal',
                'Romania', 'Russia', 'Senegal', 'Serbia', 'Singapore', 'Slovakia', 'Slovenia',
                'South_Africa', 'South_Korea', 'Spain', 'Sri_Lanka', 'Sweden', 'Switzerland', 'Taiwan',
                'Thailand', 'Turkey', 'Ukraine', 'United_Arab_Emirates', 'United_States', 'Uruguay',
                'Vietnam', 'Venuzela'
            ]
        elif lp == "blue":
            remove = ['Austria','Belgium','Bulgaria','Croatia','Czechia','Denmark','Estonia','Finland','France',
    'Germany','Greece','Hungary','Ireland','Italy','Latvia','Lithuania','Luxembourg','Poland',
    'Portugal','Romania','Slovakia','Slovenia','Spain','Sweden']

        elif lp == "other": 
            remove =['United_Kingdom', 'Netherlands', 'Colombia',
    'Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Czechia', 'Denmark', 'Estonia',
    'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Ireland', 'Italy', 'Latvia',
    'Lithuania', 'Luxembourg', 'Poland', 'Portugal', 'Romania', 'Slovakia', 'Slovenia',
    'Spain', 'Sweden']
        else:
            remove = []
        self.countries = [c for c in self.countries if c not in remove]

    def filter_by_writing(self, lang):
        if lang == "english":
            remove = [
                'Albania', 'Andorra', 'Argentina', 'Austria', 'Bangladesh', 'Belgium', 'Bhutan', 'Bolivia',
                'Botswana', 'Brazil', 'Bulgaria', 'Cambodia', 'Chile', 'Colombia', 'Croatia', 'Czechia',
                'Denmark', 'Dominican_Republic', 'Ecuador', 'Estonia', 'Eswatini', 'Finland', 'France',
                'Germany', 'Ghana', 'Greece', 'Greenland', 'Guatemala', 'Hungary', 'Iceland', 'Indonesia',
                'Ireland', 'Israel', 'Italy', 'Japan', 'Jordan', 'Kenya', 'Kyrgyzstan', 'Latvia',
                'Lithuania', 'Luxembourg', 'Malaysia', 'Mexico', 'Mongolia', 'Montenegro', 'Netherlands',
                'Nigeria', 'North_Macedonia', 'Norway', 'Panama', 'Peru', 'Philippines', 'Poland',
                'Portugal', 'Romania', 'Russia', 'Senegal', 'Serbia', 'Singapore', 'Slovakia', 'Slovenia',
                'South_Korea', 'Spain', 'Sri_Lanka', 'Sweden', 'Switzerland', 'Taiwan', 'Thailand',
                'Turkey', 'Ukraine', 'United_Arab_Emirates', 'Uruguay', 'Vietnam', 'Venuzela'
            ]
        elif lang == "european":
            remove = [
                'Argentina', 'Australia', 'Bangladesh', 'Bhutan', 'Bolivia', 'Botswana', 'Brazil', 'Bulgaria',
                'Cambodia', 'Canada', 'Chile', 'Colombia', 'Dominican_Republic', 'Ecuador', 'Eswatini', 'Ghana',
                'Greenland', 'Guatemala', 'Indonesia', 'Ireland', 'Israel', 'Japan', 'Jordan', 'Kenya', 'Kyrgyzstan',
                'Lesotho', 'Malaysia', 'Mexico', 'Mongolia', 'New_Zealand', 'Nigeria', 'North_Macedonia', 'Panama',
                'Peru', 'Philippines', 'Russia', 'Senegal', 'Serbia', 'Singapore', 'South_Africa', 'South_Korea',
                'Sri_Lanka', 'Taiwan', 'Thailand', 'Ukraine', 'United_Arab_Emirates', 'United_Kingdom',
                'United_States', 'Uruguay', 'Vietnam', 'Venuzela'
            ]
        elif lang == "cyrilic":
            remove = [
                'Albania', 'Andorra', 'Argentina', 'Australia', 'Austria', 'Bangladesh', 'Belgium', 'Bhutan',
                'Bolivia', 'Botswana', 'Brazil', 'Cambodia', 'Canada', 'Chile', 'Colombia', 'Croatia', 'Czechia',
                'Denmark', 'Dominican_Republic', 'Ecuador', 'Estonia', 'Eswatini', 'Finland', 'France', 'Germany',
                'Ghana', 'Greece', 'Greenland', 'Guatemala', 'Hungary', 'Iceland', 'Indonesia', 'Ireland', 'Israel',
                'Italy', 'Japan', 'Jordan', 'Kenya', 'Latvia', 'Lesotho', 'Lithuania', 'Luxembourg', 'Malaysia',
                'Mexico', 'Montenegro', 'Netherlands', 'New_Zealand', 'Nigeria', 'Norway', 'Panama', 'Peru',
                'Philippines', 'Poland', 'Portugal', 'Romania', 'Senegal', 'Serbia', 'Singapore', 'Slovakia',
                'Slovenia', 'South_Africa', 'South_Korea', 'Spain', 'Sri_Lanka', 'Sweden', 'Switzerland', 'Taiwan',
                'Thailand', 'Turkey', 'Ukraine', 'United_Arab_Emirates', 'United_Kingdom', 'United_States', 'Uruguay',
                'Vietnam', 'Venuzela'
            ]
        elif lang == "spanish":
            remove = [
                'Albania', 'Andorra', 'Australia', 'Austria', 'Bangladesh', 'Belgium', 'Bhutan', 'Botswana',
                'Brazil', 'Bulgaria', 'Cambodia', 'Canada', 'Croatia', 'Czechia', 'Denmark', 'Estonia', 'Eswatini',
                'Finland', 'France', 'Germany', 'Ghana', 'Greece', 'Greenland', 'Hungary', 'Iceland',
                'Indonesia', 'Ireland', 'Israel', 'Italy', 'Japan', 'Jordan', 'Kenya', 'Kyrgyzstan',
                'Latvia', 'Lesotho', 'Lithuania', 'Luxembourg', 'Malaysia', 'Mongolia', 'Montenegro',
                'Netherlands', 'New_Zealand', 'Nigeria', 'North_Macedonia', 'Norway', 'Philippines',
                'Poland', 'Portugal', 'Romania', 'Russia', 'Senegal', 'Serbia', 'Singapore', 'Slovakia',
                'Slovenia', 'South_Africa', 'South_Korea', 'Sri_Lanka', 'Sweden', 'Switzerland', 'Taiwan',
                'Thailand', 'Turkey', 'Ukraine', 'United_Arab_Emirates', 'United_Kingdom', 'United_States',
                'Vietnam'
            ]
        elif lang == "characters":  # characters
            remove = [
                'Albania', 'Andorra', 'Argentina', 'Australia', 'Austria', 'Belgium', 'Bolivia', 'Botswana',
                'Brazil', 'Bulgaria', 'Canada', 'Chile', 'Colombia', 'Croatia', 'Czechia', 'Denmark',
                'Dominican_Republic', 'Ecuador', 'Estonia', 'Eswatini', 'Finland', 'France', 'Germany',
                'Ghana', 'Greece', 'Greenland', 'Guatemala', 'Hungary', 'Iceland', 'Indonesia', 'Ireland',
                'Italy', 'Kenya', 'Kyrgyzstan', 'Latvia', 'Lesotho', 'Lithuania', 'Luxembourg', 'Malaysia',
                'Mexico', 'Mongolia', 'Montenegro', 'Netherlands', 'New_Zealand', 'Nigeria', 'North_Macedonia',
                'Norway', 'Panama', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Romania', 'Russia', 'Senegal',
                'Serbia', 'Slovakia', 'Slovenia', 'South_Africa', 'Spain', 'Sweden', 'Switzerland', 'Turkey',
                'Ukraine', 'United_Kingdom', 'United_States', 'Uruguay', 'Vietnam', 'Venuzela', 'Bangladesh',
                'Bhutan', 'Cambodia', 'Israel', 'Jordan', 'Singapore', 'Sri_Lanka', 'Thailand',
                'United_Arab_Emirates'
            ]
        else:
            remove = []
        self.countries = [c for c in self.countries if c not in remove]


if __name__ == "__main__":
    app = CountryDeterminer()
    app.mainloop()