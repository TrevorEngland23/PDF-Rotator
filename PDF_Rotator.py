import PyPDF2
import tkinter as tk
from tkinter import filedialog, messagebox

def rotate_pdf():
    input_file = filedialog.askopenfilename(title="Select a PDF to Rotate", filetypes=[("PDF Files", "*.pdf")])

    if not input_file:
        return

    output_file = input_file.replace('.pdf', '_portrait.pdf')

    try:
        with open(input_file, 'rb') as pdfIn, open(output_file, 'wb') as pdfOut:
            pdfReader = PyPDF2.PdfReader(pdfIn)
            pdfWriter = PyPDF2.PdfWriter()

            for page in pdfReader.pages:
                if page.rotation > 0:
                    current_rotation = page.rotation
                else:
                    page.rotation = 0

                if current_rotation == 90:
                    page.rotate(-90) 
                elif current_rotation == 270:
                    page.rotate(90) 
                elif current_rotation == 180:
                    page.rotate(180)

                pdfWriter.add_page(page)

            pdfWriter.write(pdfOut)

        messagebox.showinfo("Success", f"Portrait PDF saved as:\n{output_file}")

    except FileNotFoundError:
        messagebox.showerror("Error", "File not found!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{e}")

root = tk.Tk()
root.title("PDF Rotator")
root.geometry("300x300")

btn_rotate = tk.Button(root, text="Select PDF to Rotate", command=rotate_pdf, font=("Arial", 12), padx=10, pady=10)
btn_rotate.pack(expand=True)

root.mainloop()