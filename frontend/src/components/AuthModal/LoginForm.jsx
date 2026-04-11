import { useState } from 'react';
import { loginUser } from '../../services/authApi';
import styles from './AuthModal.module.css';

import logo from '../../assets/logo.svg';

export default function LoginForm({ onClose }) {
  const [formData, setFormData] = useState({
    email: '',
    password: '',
  });

  const [error, setError] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleChange = event => {
    const { name, value } = event.target;

    setFormData(prev => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleSubmit = async event => {
    event.preventDefault();
    setError('');

    try {
      setIsLoading(true);

      const data = await loginUser({
        email: formData.email,
        password: formData.password,
      });

      console.log('Успешный вход:', data);

      if (data.token) {
        localStorage.setItem('token', data.token);
        console.log('Токен сохранен в localStorage:', data.token);
      }

      if (data.user) {
        localStorage.setItem('user', JSON.stringify(data.user));
        console.log('Пользователь сохранен в localStorage:', data.user);
      }

      onClose();
    } catch (err) {
      console.error('Ошибка входа:', err.message);
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <form className={styles.form} onSubmit={handleSubmit}>
      <div className={styles.imageWrapper}>
        <img src={logo} alt="animals" className={styles.authImage} />
      </div>

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

      {error && <p className={styles.error}>{error}</p>}

      <button
        className={styles.submitButton}
        type="submit"
        disabled={isLoading}
      >
        {isLoading ? 'Завантаження...' : 'Увійти >'}
      </button>
    </form>
  );
}
