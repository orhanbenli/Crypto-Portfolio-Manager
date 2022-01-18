from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
import pickle


root = Tk()
root.title('Crypto Portfolio Manager')
root.iconbitmap('file:///Users/orhanbenli/Desktop/py/t.ico')
root.geometry("650x500")

# Let's define the Font
crypto_font = Font(
	family="Georgia",
	size=28,
	weight="bold")

# Let's create the Frame
crypto_frame = Frame(root)
crypto_frame.pack(pady=8)

# Let's create the Listbox
crypto_list = Listbox(crypto_frame,
	font=crypto_font,
	width=30,
	height=10,
	bg="#F0FFFF",
	bd=1,
	fg="black",
	highlightthickness=0,
	selectbackground="#D3D3D3",
	activestyle="none")

crypto_list.pack(side=LEFT, fill=BOTH)

# Let's create a sample list
my_crypto = ["Bitcoin (BTC)", "Ethereum (ETH)", "Cardano (ADA)", "Solana (SOL)", "Polkadot (DOT)"]
# Then, add sample list to list box
for coin in my_crypto:
	crypto_list.insert(END, coin)

# Let's create the Scrollbar
crypto_scrollbar = Scrollbar(crypto_frame)
crypto_scrollbar.pack(side=RIGHT, fill=BOTH)

# Let's add the Scrollbar
crypto_list.config(yscrollcommand=crypto_scrollbar.set)
crypto_scrollbar.config(command=crypto_list.yview)

# Let's create the Entry Box
crypto_entry = Entry(root, font=("Georgia", 25), width=35)
crypto_entry.pack(pady=18)

# Let's create the Button Frame
b_frame = Frame(root)
b_frame.pack(pady=18)

# Let's create some useful Functions
def delete_coin():
	crypto_list.delete(ANCHOR)

def add_coin():
	crypto_list.insert(END, crypto_entry.get())
	crypto_entry.delete(0, END)

def cross_off_coin():
	# First, cross off item
	crypto_list.itemconfig(
		crypto_list.curselection(),
		fg="#D3D3D3")
	# Second, get rid of the highlight
	crypto_list.selection_clear(0, END)

def uncross_coin():
	# First, uncross off item
	crypto_list.itemconfig(
		crypto_list.curselection(),
		fg="black")
	# Second, get rid of the highlight
	crypto_list.selection_clear(0, END)

def delete_crossed_coin():
	count = 0
	while count < crypto_list.size():
		if crypto_list.itemcget(count, "fg") == "#D3D3D3":
			crypto_list.delete(crypto_list.index(count))
		
		else: 
			count += 1

def save_lst():
	crypto_file_name = filedialog.asksaveasfilename(
		initialdir="file:///Users/orhanbenli/Desktop/py",
		title="Save Crypto File",
		filetypes=(
			("Dat Files", "*.dat"), 
			("All Files", "*.*"))
		)

	if crypto_file_name:
		if crypto_file_name.endswith(".dat"):
			pass
		else:
			crypto_file_name = f'{crypto_file_name}.dat'

		# Let's delete crossed off coins before we save them
		count = 0
		while count < crypto_list.size():
			if crypto_list.itemcget(count, "fg") == "#D3D3D3":
				crypto_list.delete(crypto_list.index(count))
			
			else: 
				count += 1

		# Let's get all the crypto stuff from our list
		crypto_stuff = crypto_list.get(0, END)

		# Now, let's open the file
		output_crypto_file = open(crypto_file_name, 'wb')

		# Then, we add the crypto stuff to the file
		pickle.dump(crypto_stuff, output_crypto_file)

def open_lst():
	crypto_file_name = filedialog.askopenfilename(
		initialdir="file:///Users/orhanbenli/Desktop/py",
		title="Open File",
		filetypes=(
			("Dat Files", "*.dat"), 
			("All Files", "*.*"))
		)

	if crypto_file_name:
		# We need to delete currently open list
		crypto_list.delete(0, END)

		# Then, let's open the file
		crypto_input_file = open(crypto_file_name, 'rb')

		# Now, let's load the data from the file
		crypto_stuff = pickle.load(crypto_input_file)

		# Finally, let's output crypto stuff to the screen
		for crypto in crypto_stuff:
			crypto_list.insert(END, crypto)

def delete_lst():
	crypto_list.delete(0, END)

# Let's create our Menu
crypto_menu = Menu(root)
root.config(menu=crypto_menu)

# Then, let's add some items to our menu
crypto_file_menu = Menu(crypto_menu, tearoff=False)
crypto_menu.add_cascade(label="File", menu=crypto_file_menu)

# And add dropdown items
crypto_file_menu.add_command(label="Save List", command=save_lst)
crypto_file_menu.add_command(label="Open List", command=open_lst)
crypto_file_menu.add_separator()
crypto_file_menu.add_command(label="Clear List", command=delete_lst)


# Let's add some Buttons
delete_b = Button(b_frame, text="Delete Coin", command=delete_coin)
add_b = Button(b_frame, text="Add Coin", command=add_coin)
cross_off_b = Button(b_frame, text="Cross Off Coin", command=cross_off_coin)
uncross_b = Button(b_frame, text="Uncross Coin", command=uncross_coin)
delete_crossed_b = Button(b_frame, text="Delete Crossed Coin", command=delete_crossed_coin)

delete_b.grid(row=0, column=0)
add_b.grid(row=0, column=1, padx=18)
cross_off_b.grid(row=0, column=2)
uncross_b.grid(row=0, column=3, padx=18)
delete_crossed_b.grid(row=0, column=4)

root.mainloop()
