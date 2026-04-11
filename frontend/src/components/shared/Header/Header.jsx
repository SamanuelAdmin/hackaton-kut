import React, { useState } from 'react';
import { Link } from 'react-router';

import logo from '../../../assets/logo.svg';
import login from '../../../assets/login.svg';
import styles from './Header.module.css';
import AuthModal from '../../AuthModal/AuthModal';

export const Header = () => {
  const [isAuthOpen, setIsAuthOpen] = useState(false);

  return (
    <>
      <header className={styles.header}>
        <div className={styles.headerInner}>
          <div className={styles.logo}>
            <Link to="/" className={styles.logoLink}>
              <img src={logo} alt="logo" />
              <p>Dnipro animals</p>
            </Link>
          </div>
          <nav>
            <ul className={styles.list}>
              <li>
                <Link to="/catalog" className={styles.navLink}>
                  Усі тваринки
                </Link>
              </li>
              <li>
                <Link to="/swipe" className={styles.navLink}>
                  ЛапоСвайп
                </Link>
              </li>
              <li>
                <Link to="/news" className={styles.navLink}>
                  Пости
                </Link>
              </li>
            </ul>
          </nav>
          <div className={styles.auth}>
            <button onClick={() => setIsAuthOpen(true)}>
              <img src={login} alt="auth" />
            </button>
          </div>
        </div>
      </header>
      <AuthModal isOpen={isAuthOpen} onClose={() => setIsAuthOpen(false)} />
    </>
  );
};
