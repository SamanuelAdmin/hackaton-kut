import { useEffect, useState } from "react";
import LoginForm from "./LoginForm";
import RegisterForm from "./RegisterForm";
import styles from "./AuthModal.module.css";

export default function AuthModal({ isOpen, onClose }) {
  const [mode, setMode] = useState("register");

  useEffect(() => {
    if (!isOpen) return;

    const handleEsc = (event) => {
      if (event.key === "Escape") {
        onClose();
      }
    };

    document.addEventListener("keydown", handleEsc);
    document.body.style.overflow = "hidden";

    return () => {
      document.removeEventListener("keydown", handleEsc);
      document.body.style.overflow = "auto";
    };
  }, [isOpen, onClose]);

  if (!isOpen) return null;

  return (
    <div className={styles.overlay} onClick={onClose}>
      <div className={styles.modal} onClick={(event) => event.stopPropagation()}>
        <div className={styles.tabs}>
          <button
            type="button"
            className={`${styles.tab} ${mode === "register" ? styles.activeTab : ""}`}
            onClick={() => setMode("register")}
          >
            Sign in
          </button>

          <span className={styles.separator}>|</span>

          <button
            type="button"
            className={`${styles.tab} ${mode === "login" ? styles.activeTab : ""}`}
            onClick={() => setMode("login")}
          >
            Log in
          </button>
        </div>

        {mode === "register" ? (
          <RegisterForm switchToLogin={() => setMode("login")} />
        ) : (
          <LoginForm onClose={onClose} />
        )}
      </div>
    </div>
  );
}