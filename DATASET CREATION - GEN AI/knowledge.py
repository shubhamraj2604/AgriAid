CROP_RULES = {
    "Rice": {
        "soil": ["Clayey", "Clay Loam", "Loamy"],
        "ph": (5.5, 7.0),
        "rainfall": (1200, 1600),
        "temp": (22, 32),
        "yield": (2.5, 4.5),
        "methods": [
            "Transplanted paddy with puddling",
            "System of Rice Intensification (SRI)"
        ]
    },

    "Maize": {
        "soil": ["Sandy Loam", "Loamy"],
        "ph": (5.8, 7.5),
        "rainfall": (900, 1200),
        "temp": (18, 30),
        "yield": (2.0, 4.0),
        "methods": [
            "Line sowing with ridge-furrow method",
            "Rainfed maize cultivation"
        ]
    },

    "Wheat": {
        "soil": ["Loamy", "Clay Loam"],
        "ph": (6.0, 7.5),
        "rainfall": (900, 1400),
        "temp": (18, 25),
        "yield": (1.7, 3.4),
        "methods": [
            "Residual moisture-based rabi cultivation",
            "Timely sowing with balanced fertilization"
        ]
    },

    "Pulses": {
        "soil": ["Sandy Loam", "Loamy"],
        "ph": (6.0, 7.5),
        "rainfall": (800, 1100),
        "temp": (18, 28),
        "yield": (1.0, 2.0),
        "methods": [
            "Intercropping with cereals",
            "Rainfed pulse cultivation"
        ]
    }
}

NPK_LEVELS = ["Low", "Medium", "High"]
