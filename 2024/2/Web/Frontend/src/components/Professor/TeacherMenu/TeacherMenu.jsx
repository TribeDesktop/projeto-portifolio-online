import styles from './TeacherMenu.module.css';
import icons from '../../../assets/images/icons/icons';
import logos from '../../../assets/images/logos/logos';

const Menu = ({ studentName }) => {
  return (
    <div className={styles.menuContainer}>
      <div className={styles.menuLogo}>
        <img src={logos.white.src} className={styles.whiteLogo} alt={logos.white.alt} />
      </div>
      <div className={styles.menuUserInfo}>
        <div className={styles.userImage}></div>
        <h4>{studentName}</h4>
        <h6>Professora</h6>
      </div>
      <div className={styles.menuConsult}>
        <div className={styles.consultTitle}>
          <p>Início</p>
          <div className={styles.string}></div>
        </div>
        <div className={styles.consultActions}>
          <div className={styles.consultItems}>
            <img src={icons.students.src} alt={icons.students.alt} />
            <p>Alunos</p>
          </div>
          <div className={styles.consultItems}>
            <img src={icons.notas.src} alt={icons.notas.alt} />
            <p>Notas</p>
          </div>
          <div className={styles.consultItems}>
            <img src={icons.book.src} alt={icons.book.alt} />
            <p>Planejamento</p>
          </div>
          <div className={styles.consultItems}>
            <img src={icons.book.src} alt={icons.book.alt} />
            <p>Conteúdos</p>
          </div>
          <div className={styles.consultItems}>
            <img src={icons.calendar.src} alt={icons.calendar.alt} />
            <p>Calendário</p>
          </div>
        </div>
      </div>
      <div className={styles.string2}></div>
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
