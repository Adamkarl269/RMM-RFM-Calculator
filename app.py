from kivy.app import App
from kivy.lang import Builder
import json


class PyChemApp(App):

    def build(self):
        return Builder.load_file("pychem.kv")

    def cal(self):
        f = open("proton.json", "r")
        data = f.read()
        f.close()

        fux = self.root.ids.input_one.text
        sux = self.root.ids.input_two.text
        tux = self.root.ids.input_three.text

        nfux = self.root.ids.input_one_one.text
        nsux = self.root.ids.input_two_two.text
        ntux = self.root.ids.input_three_three.text

        d = json.loads(data)

        a = int(d[fux])
        b = int(d[sux])
        c = int(d[tux])

        cal = (int(nfux) * a) + (int(nsux) * b) + (int(ntux) * c)

        cl = str(cal)

        va = f""" 
        RMM/RFM {fux}{nfux}{sux}{nsux}{tux}{ntux} 
        = ({nfux} x {a}) + ({nsux} x {b}) + ({ntux} x {c})
        = {cl}"""

        self.root.ids.top_label.text = va


if __name__ == "__main__":
    PyChemApp().run()
