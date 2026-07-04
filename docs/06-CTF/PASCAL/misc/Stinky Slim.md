This writeup for **Stinky Slim** focuses on **Audio Forensics** and hidden messages within sound frequencies. I have translated the content into simple English and added reusable tags for your database.

---

# 🔊 Category: Steganography / Audio Forensics

#technique/spectrogram #technique/audio-forensics #technique/social-engineering #tool/audacity #tool/spek #category/steganography

---

## 📘 Description

**Author:** Enea Maroncelli (`@ZazaMan`)

This challenge provides a `.wav` audio file named `pieno-di-slim.wav` containing music mixed with distorted sounds. The hint suggests that "Patapim" is hiding something within the file. Since the secret is not audible, the investigation focuses on the visual representation of the sound.

---

## 🛠 Tools Used

- **Audacity / Spek:** For visualizing and analyzing audio spectrograms.
- **Discord:** For the final interaction phase (opening a support ticket).

---

## ⚙️ Methodology

### 1. Spectrogram Analysis

- **Initial Inspection:** The audio file was loaded into a spectral analysis tool.
- **Visual Discovery:** By increasing the gain and inspecting the ultra-high frequencies (above 15-17kHz), a hidden message became visually readable in the spectrogram.

### 2. Message Decoding

- The hidden text revealed a specific instruction: _"Open a ticket saying you love Blaise Pascal to get the flag"_.

### 3. Interaction

- Following the instructions, I opened a support ticket on the official server.
- Upon sending the exact phrase **"I love Blaise Pascal"**, the flag was provided by the support team.
- 
---

## 🏁 Flag

`pascalCTF{th3_k1ng_0f_th3_f0r3st_w1th_s0m3_d1rty_f3et}`