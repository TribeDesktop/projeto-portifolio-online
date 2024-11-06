import styles from './Panel.module.css';
import logos from '../../assets/images/logos/logos';

const Panel = ({ pageName, section, color }) => {
  return (
    <div className={styles.homeHeader} style={{ borderBottom: `10px solid ${color}` }}>
      <div className={styles.homeHeaderText}>
        <h1>{pageName}</h1>
        <p className={styles.sec}>{section}</p>
      </div>
      <img className={styles.homeLogo} src={logos.banner.src} alt={logos.banner.alt} />
    </div>
  );
};

export default Panel;
