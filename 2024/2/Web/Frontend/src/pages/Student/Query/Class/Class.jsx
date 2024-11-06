import styles from './Class.module.css';
import Menu from '../../../../components/Student/Menu/Menu';
import Panel from '../../../../components/Panel/Panel';

const Class = () => {
  return (
    <div className={styles.classesContainer}>
      <Menu studentName={'Ana Clara'} />
      <div className={styles.classesSideContent}>
        <Panel pageName="Painel do Aluno" section="Consultas/Aulas" color="#677C91" />
        <div className={styles.classesInfo}>
          <div className={styles.classesCard}>
            <div className={styles.classesCardTitle}>
              <p>Notas</p>
              <hr />
            </div>
            <div className={styles.classesCardTable}>
              <div className={styles.classesCardTableHeader}>
                <div className={styles.classesHeader}>
                  <span>Segunda</span>
                  <span>Terça</span>
                  <span>Quarta</span>
                  <span>Quinta</span>
                  <span>Sexta</span>
                </div>
              </div>
              <div className={styles.classesCardTableBody}>
                <div className={styles.classesBody}>
                  <div className={styles.classesWeekdayBody}>
                    <div className={styles.classesDay}>
                      <span>Materia 1</span>
                      <p>18h30 - 19h20</p>
                    </div>
                    <div className={styles.classesDay}>
                      <span>Materia 1</span>
                      <p>18h30 - 19h20</p>
                    </div>
                    <div className={styles.classesDay}>
                      <span>Materia 1</span>
                      <p>18h30 - 19h20</p>
                    </div>
                    <div className={styles.classesDay}>
                      <span>Materia 1</span>
                      <p>18h30 - 19h20</p>
                    </div>
                    <div className={styles.classesDay}>
                      <span>Materia 1</span>
                      <p>18h30 - 19h20</p>
                    </div>
                  </div>

                  <div className={styles.classesWeekdayBody}>
                    <div className={styles.classesDay}>
                      <span>Materia 2</span>
                      <p>19h20 - 20h10</p>
                    </div>
                    <div className={styles.classesDay}>
                      <span>Materia 2</span>
                      <p>19h20 - 20h10</p>
                    </div>
                    <div className={styles.classesDay}>
                      <span>Materia 2</span>
                      <p>19h20 - 20h10</p>
                    </div>
                    <div className={styles.classesDay}>
                      <span>Materia 2</span>
                      <p>19h20 - 20h10</p>
                    </div>
                    <div className={styles.classesDay}>
                      <span>Materia 2</span>
                      <p>19h20 - 20h10</p>
                    </div>
                  </div>

                  <div className={styles.classesWeekdayBody}>
                    <div className={styles.classesDay}>
                      <span>Materia 3</span>
                      <p>20h10 - 21h00</p>
                    </div>
                    <div className={styles.classesDay}>
                      <span>Materia 3</span>
                      <p>20h10 - 21h00</p>
                    </div>
                    <div className={styles.classesDay}>
                      <span>Materia 3</span>
                      <p>20h10 - 21h00</p>
                    </div>
                    <div className={styles.classesDay}>
                      <span>Intervalo</span>
                      <p>20h10 - 21h00</p>
                    </div>
                    <div className={styles.classesDay}>
                      <span>Materia 3</span>
                      <p>20h10 - 21h00</p>
                    </div>
                  </div>

                  <div className={styles.classesWeekdayBody}>
                    <div className={styles.classesDay}>
                      <span>Intervalo</span>
                      <p>21h00 - 21h20</p>
                    </div>
                    <div className={styles.classesDay}>
                      <span>Intervalo</span>
                      <p>21h00 - 21h20</p>
                    </div>
                    <div className={styles.classesDay}>
                      <span>Intervalo</span>
                      <p>21h00 - 21h20</p>
                    </div>
                    <div className={styles.classesDay}>
                      <span>Intervalo</span>
                      <p>21h00 - 21h20</p>
                    </div>
                    <div className={styles.classesDay}>
                      <span>Intervalo</span>
                      <p>21h00 - 21h20</p>
                    </div>
                  </div>

                  <div className={styles.classesWeekdayBody}>
                    <div className={styles.classesDay}>
                      <span>Materia 4</span>
                      <p>21h20 - 22h10</p>
                    </div>
                    <div className={styles.classesDay}>
                      <span>Materia 4</span>
                      <p>21h20 - 22h10</p>
                    </div>
                    <div className={styles.classesDay}>
                      <span>Materia 4</span>
                      <p>21h20 - 22h10</p>
                    </div>
                    <div className={styles.classesDay}>
                      <span>Materia 4</span>
                      <p>21h20 - 22h10</p>
                    </div>
                    <div className={styles.classesDay}>
                      <span>Materia 4</span>
                      <p>21h20 - 22h10</p>
                    </div>
                  </div>

                  <div className={styles.classesWeekdayBody}>
                    <div className={styles.classesDay}>
                      <span>Materia 5</span>
                      <p>22h10 - 23h00</p>
                    </div>
                    <div className={styles.classesDay}>
                      <span>Materia 5</span>
                      <p>22h10 - 23h00</p>
                    </div>
                    <div className={styles.classesDay}>
                      <span>Materia 5</span>
                      <p>22h10 - 23h00</p>
                    </div>
                    <div className={styles.classesDay}>
                      <span>Materia 5</span>
                      <p>22h10 - 23h00</p>
                    </div>
                    <div className={styles.classesDay}>
                      <span>Materia 5</span>
                      <p>22h10 - 23h00</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Class;
