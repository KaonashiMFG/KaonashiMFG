print("==== KONVERSI SUHU ====")

farenheitToKelvin = int(input("Farenheit -> Kelvin | ... Farenheit? "))
kelvin = (farenheitToKelvin + 459.67) * (5/9)
print(kelvin)

kelvinToFarenheit = int(input("Kelvin -> Farenheit | ... Kelvin? "))
farenheit = 1.8 * (kelvinToFarenheit - 273) +32
print(farenheit)

print("==== KONVERSI SUHU LANGSUNG====")

