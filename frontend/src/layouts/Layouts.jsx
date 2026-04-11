import React from 'react';
import { Outlet } from 'react-router';
import { Header } from '../components/shared/Header/Header';

import styles from './Layouts.module.css';

export const Layouts = () => {
  return (
    <div className={styles.container}>
      <Header />
      <main>
        <Outlet />
      </main>
    </div>
  );
};
