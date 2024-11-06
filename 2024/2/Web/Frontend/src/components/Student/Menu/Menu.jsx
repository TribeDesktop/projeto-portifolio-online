import styles from './Menu.module.css';
import icons from '../../../assets/images/icons/icons';
import logos from '../../../assets/images/logos/logos';
import { Link } from 'react-router-dom';

const Menu = ({ studentName }) => {
  return (
    <div className={styles.menuContainer}>
      <div className={styles.menuLogo}>
        <img src={logos.white.src} id={styles.whiteLogo} alt={logos.white.alt} />
      </div>
      <div className={styles.menuUserInfo}>
        <div id={styles.userImageMenu}></div>
        <p>{studentName}</p>
      </div>
      <div className={styles.menuConsult}>
        <div className={styles.consultTitle}>
          <Link id={styles.title} to={'/student/query'}>
            <p>Consultas</p>
          </Link>
          <div id={styles.string}></div>
        </div>
        <div className={styles.consultActions}>
          <div className={styles.consultItems}>
            <img src={icons.x.src} alt={icons.x.alt} />
            <Link id={styles.items} to={'/student/query/absence'}>
              <p>Faltas</p>
            </Link>
          </div>
          <div className={styles.consultItems}>
            <img src={icons.star.src} alt={icons.star.alt} />
            <p>Notas</p>
          </div>
          <div className={styles.consultItems}>
            <img src={icons.clock.src} alt={icons.clock.alt} />
            <p>Aulas</p>
          </div>
          <div className={styles.consultItems}>
            <img src={icons.history.src} alt={icons.history.alt} />
            <p>Histórico</p>
          </div>
        </div>
      </div>
      <div className={styles.menuRegistration}>
        <div className={styles.registryTitle}>
          <p>Matrícula</p>
          <div id={styles.string}></div>
        </div>
        <div className={styles.registryActions}>
          <div className={styles.registryItems}>
            <img src={icons.book.src} alt={icons.book.alt} />
            <p>Disciplinas</p>
          </div>
          <div className={styles.registryItems}>
            <img src={icons.danger.src} alt={icons.danger.alt} />
            <p>Pendências</p>
          </div>
        </div>
      </div>
      <div id={styles.string2}></div>
      <div className={styles.menuActions}>
        <div className={styles.menuActionsImg}>
          <img src={icons.gear.src} alt={icons.gear.alt} />
          <p>Configurações</p>
        </div>
        <div className={styles.menuActionsImg}>
          <img src={icons.quit.src} alt={icons.quit.alt} />
          <p>Sair</p>
        </div>
      </div>
      <div></div>
    </div>
  );
};

export default Menu;
