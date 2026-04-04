import { useState } from "react";
import { registerUser } from "../../services/authApi";
import styles from "./AuthModal.module.css";

export default function RegisterForm({ switchToLogin }) {
  const [formData, setFormData] = useState({
    full_name: "",
    email: "",
    password: "",
    confirmPassword: "",
  });

  const [error, setError] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const handleChange = (event) => {
    const { name, value } = event.target;

    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    setError("");

    if (formData.password !== formData.confirmPassword) {
      setError("Паролі не співпадають");
      return;
    }

    try {
      setIsLoading(true);

      const data = await registerUser({
        full_name: formData.full_name,
        email: formData.email,
        clear_password: formData.password,
      });

      console.log("Успешная регистрация:", data);

      switchToLogin();
    } catch (err) {
      console.error("Ошибка регистрации:", err.message);
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <form className={styles.form} onSubmit={handleSubmit}>
      <label className={styles.label}>Ім'я:</label>
      <input
        className={styles.input}
        type="text"
        name="full_name"
        value={formData.full_name}
        onChange={handleChange}
        required
      />

      <label className={styles.label}>Електронна пошта:</label>
      <input
        className={styles.input}
        type="email"
        name="email"
        value={formData.email}
        onChange={handleChange}
        required
      />

      <label className={styles.label}>Пароль:</label>
      <input
        className={styles.input}
        type="password"
        name="password"
        value={formData.password}
        onChange={handleChange}
        required
      />

      <label className={styles.label}>Підтвердити пароль:</label>
      <input
        className={styles.input}
        type="password"
        name="confirmPassword"
        value={formData.confirmPassword}
        onChange={handleChange}
        required
      />

      {error && <p className={styles.error}>{error}</p>}

      <button className={styles.submitButton} type="submit" disabled={isLoading}>
        {isLoading ? "Завантаження..." : "Створити >"}
      </button>
    </form>
  );
}