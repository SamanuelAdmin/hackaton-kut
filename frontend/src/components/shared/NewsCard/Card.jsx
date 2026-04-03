import React from 'react';

import styles from './Card.module.css';
export const Card = ({ image, title, text }) => {
  return (
    <article className={styles.card}>
      <img src={image} alt={title} className={styles.image} />

      <div className={styles.overlay}>
        <h3 className={styles.title}>{title}</h3>
        <p className={styles.text}>{text}</p>
      </div>
    </article>
  );
};
