# VTXEngine 🎮

**VTXEngine** is a modular, from-scratch game engine built in Python by [CODE_BOSS](https://github.com/Raphael-Varghese). It simulates the architecture of professional game engines like Unity or Unreal, but is designed to run offline, without dependencies, and in clearly defined development phases.

---

## 🚀 Project Goals

- Build a complete game engine from scratch using Python  
- Simulate real-world engine architecture: Core, Math, Graphics, Scene, etc.  
- Avoid external libraries and imports—manual loading only  
- Maintain clean modular folder structure  
- Commit each phase as a milestone  

---

## 📦 Folder Structure

VTXEngine/  
├── main.py  
├── engine/  
│   ├── core/  
│   │   ├── logger.py  
│   │   └── timer.py  
│   └── math/  
│       ├── vector2.py  
│       └── vector3.py  

Each module is manually loaded using Python’s `exec()` function to avoid import errors and keep the engine portable across restricted environments.

---

## 🧱 Development Phases

Phase 1 – Core system: Logger and Timer modules  
Phase 2 – Math module: Vector2 and Vector3 classes  
Phase 3 – Graphics module: Software rasterizer and pixel simulation  
Phase 4 – Scene system: Entity-component architecture  
Phase 5 – Input and UI systems  
Phase 6 – Audio simulation  
Phase 7 – Scripting and editor tools  
Phase 8 – Asset pipeline and resource management  
Phase 9 – Networking and multiplayer logic  
Phase 10 – Final polish and demo scenes  

Each phase is committed separately and labeled for easy reference.

---

## 🧪 How to Run

Make sure you're in the root folder of the project, then run:

python main.py

You’ll see simulated engine output in the terminal, including frame updates, vector math, and timing logs.

---

## 🛠️ Manual Module Loading

Modules are loaded using Python’s `exec()` function:

with open("engine/core/logger.py", "r") as f:  
 exec(f.read(), logger_globals)

This avoids import errors and keeps the engine portable across environments with limited permissions.

---

## 👨‍💻 Author

Built by [CODE_BOSS](https://github.com/Raphael-Varghese)

---

## 📌 License

This project is open-source and free to use for educational and personal development purposes. No external libraries or dependencies are used.

---

## 🤝 Contributing

Want to contribute to future phases? Fork the repo, build your module, and submit a pull request with a clear description of your changes.
