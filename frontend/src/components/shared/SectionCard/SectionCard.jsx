import React from 'react';
import { Link } from 'react-router';
import { Button } from '../../ui/Button';
import styles from './SectionCard.module.css';

export const SectionCard = ({ title, btnText, children, to }) => {
  return (
    <div className={styles.section}>
      <div className={styles.header}>
        <h2>{title}</h2>
        <Link to={to}>
          <Button>{btnText}</Button>
        </Link>
      </div>
      <div>{children}</div>
    </div>
  );
};
