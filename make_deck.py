from reportlab.lib.pagesizes import landscape
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

TITLE = "ATRC School Program — Directed Energy Challenge"
PROJECT = "DE-RescueBeam: Wireless Power Beam for Emergency Sensors & Rescue Drones"

slides = [
    ("Title",
     [PROJECT,
      "Python-only concept prototype + simulation",
      "Goal: extend rescue mission runtime by beaming power safely to devices"]),
    ("The Problem",
     ["During disasters, batteries fail first:",
      "• Sensors lose power → no location/temperature data",
      "• Drones land early → less search coverage",
      "• Teams risk lives replacing batteries manually"]),
    ("Directed Energy Concept",
     ["Directed energy = focused beam sent to a target at a distance",
      "Our use (civilian): beam delivers power through air to devices",
      "Candidate technologies: laser power transfer / microwave power transfer"]),
    ("How It Works (System)",
     ["1) Detect devices with low battery",
      "2) Prioritize the lowest battery within range",
      "3) Aim beam and charge for a short burst",
      "4) Apply safety constraints (no-beam zones)"]),
    ("Safety & Ethics",
     ["Safety rule in prototype: Human Safety Zone → beam disabled inside it",
      "Future: eye-safe wavelengths, power limits, beam shutoff, tracking validation",
      "Purpose: humanitarian rescue support, not weaponization"]),
    ("Python Prototype Demonstration",
     ["Simulation shows:",
      "• moving drones + stationary sensors",
      "• battery drain over time",
      "• beam selects lowest battery and charges it",
      "• prevents charging inside protected zone"]),
    ("Impact",
     ["• Longer drone flight time = wider search area",
      "• Continuous sensor data in remote locations",
      "• Faster rescue response and lower risk to responders",
      "• Useful for desert rescue, floods, and remote infrastructure"]),
    ("Future Work",
     ["• Add multi-station scheduling (smart grid of beams)",
      "• Add weather attenuation model (dust, fog)",
      "• Add cost/efficiency trade-offs and optimization",
      "• Hardware roadmap: tracking + safety interlocks + certified power limits"]),
]

def make_pdf(filename="DE_RescueBeam_ATRC_Deck.pdf"):
    w, h = landscape((29.7*cm, 21.0*cm))  # A4 landscape in cm
    c = canvas.Canvas(filename, pagesize=(w, h))

    for title, bullets in slides:
        c.setFont("Helvetica-Bold", 22)
        c.drawString(2.2*cm, h-2.2*cm, TITLE)

        c.setFont("Helvetica-Bold", 28)
        c.drawString(2.2*cm, h-4.2*cm, title)

        y = h-6.2*cm
        c.setFont("Helvetica", 18)
        for b in bullets:
            c.drawString(3.0*cm, y, b)
            y -= 1.1*cm

        c.showPage()

    c.save()
    print("Saved:", filename)

if __name__ == "__main__":
    make_pdf()
