from tkinter import *

root = Tk()
inBox = StringVar()
outBox = StringVar(root, value="Waiting")
v = IntVar()

DNA = {
    "a": "t",
    "t": "a",
    "g": "c",
    "c": "g",
    "A": "T",
    "T": "A",
    "G": "C",
    "C": "G",
    "u": "t",
    "U": "T"
}
RNA = {
    "a": "u",
    "t": "a",
    "g": "c",
    "c": "g",
    "A": "U",
    "T": "A",
    "G": "C",
    "C": "G"}

codonTable = {
    'G': {
        'G': {
            'G': 'Gly',
            'U': 'Gly',
            'C': 'Gly',
            'A': 'Gly'
        },
        'U': {
            'G': 'Val',
            'U': 'Val',
            'C': 'Val',
            'A': 'Val'
        },
        'C': {
            'G': 'Ala',
            'U': 'Ala',
            'C': 'Ala',
            'A': 'Ala'
        },
        'A': {
            'G': 'Glu',
            'U': 'Asp',
            'C': 'Asp',
            'A': 'Glu'
        }
    },
    'U': {
        'G': {
            'G': 'Trp',
            'U': 'Cys',
            'C': 'Cys',
            'A': 'Stop'
        },
        'U': {
            'G': 'Leu',
            'U': 'Phe',
            'C': 'Phe',
            'A': 'Leu'
        },
        'C': {
            'G': 'Ser',
            'U': 'Ser',
            'C': 'Ser',
            'A': 'Ser'
        },
        'A': {
            'G': 'Stop',
            'U': 'Tyr',
            'C': 'Tyr',
            'A': 'Stop'
        }
    },
    'C': {
        'G': {
            'G': 'Arg',
            'U': 'Arg',
            'C': 'Arg',
            'A': 'Arg'
        },
        'U': {
            'G': 'Leu',
            'U': 'Leu',
            'C': 'Leu',
            'A': 'Leu'
        },
        'C': {
            'G': 'Pro',
            'U': 'Pro',
            'C': 'Pro',
            'A': 'Pro'
        },
        'A': {
            'G': 'Gln',
            'U': 'His',
            'C': 'His',
            'A': 'Gln'
        }
    },
    'A': {
        'G': {
            'G': 'Arg',
            'U': 'Ser',
            'C': 'Ser',
            'A': 'Arg'
        },
        'U': {
            'G': 'Met',
            'U': 'Ile',
            'C': 'Ile',
            'A': 'Ile'
        },
        'C': {
            'G': 'Thr',
            'U': 'Thr',
            'C': 'Thr',
            'A': 'Thr'
        },
        'A': {
            'G': 'Lys',
            'U': 'Asn',
            'C': 'Asn',
            'A': 'Lys'
        }
    }
}


def convert():
    raw = inBox.get()
    setting = v.get()
    output = ''
    if setting == 0:
        for x in range(len(raw)):
            if raw[x] in DNA:
                output = output + (DNA[raw[x]])
            else:
                output = output + (raw[x])
    elif setting == 1:
        for x in range(len(raw)):
            if raw[x] in RNA:
                output = output + (RNA[raw[x]])
            else:
                output = output + (raw[x])
    elif setting == 2:
        output = codon(raw)
    else:
        print('oh no ' + raw + str(v))
    outBox.set(value=output)
    root.clipboard_clear()
    root.clipboard_append(output)
    # print(output)


def codon(raw):
    output = ''
    raw = raw.upper()
    if 'T' in raw:
        raw2 = ''
        for x in range(len(raw)):
            if raw[x] in RNA:
                raw2 = raw2 + (RNA[raw[x]])
            else:
                raw2 = raw2 + (raw[x])
        # print('converted')
        output = output + codonTable[raw2[0]][raw2[1]][raw2[2]]
    else:
        output = output + codonTable[raw[0]][raw[1]][raw[2]]
    return output


root.title('DNA Swapper')
txt = Entry(root, textvariable=inBox).grid(row=0, column=0)
result = Entry(state=DISABLED, textvariable=outBox).grid(row=0, column=2)
Radiobutton(root, text='DNA', variable=v, value=0).grid(row=1, column=0, sticky=W)
Radiobutton(root, text='RNA', variable=v, value=1).grid(row=1, column=0, sticky=E)
Radiobutton(root, text='Codon', variable=v, value=2).grid(row=1, column=1, sticky=E)
button = Button(root, text='Convert', command=convert).grid(row=1, column=2)
root.mainloop()
