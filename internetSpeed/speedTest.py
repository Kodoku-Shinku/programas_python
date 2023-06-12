import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from speedtest import Speedtest, ConfigRetrievalError


class SpeedMeasurementThread(QThread):
    measurement_done = pyqtSignal(float)

    def __init__(self, download=True, parent=None):
        super().__init__(parent)
        self.download = download

    def run(self):
        try:
            speed_test = Speedtest()
            speed_test.get_best_server()

            if self.download:
                speed = speed_test.download(threads=None) / 10**6  # Convertir a megabits por segundo
            else:
                speed = speed_test.upload(threads=None) / 10**6  # Convertir a megabits por segundo

            self.measurement_done.emit(speed)
        except ConfigRetrievalError:
            self.measurement_done.emit(-1)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Medición de Velocidad de Internet")
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.label_result = QLabel()
        self.layout.addWidget(self.label_result)

        self.button_measure_download = QPushButton("Medir Velocidad de Descarga")
        self.button_measure_download.clicked.connect(self.measure_download_speed)
        self.layout.addWidget(self.button_measure_download)

        self.button_measure_upload = QPushButton("Medir Velocidad de Subida")
        self.button_measure_upload.clicked.connect(self.measure_upload_speed)
        self.layout.addWidget(self.button_measure_upload)

        self.speed_measurement_thread = None

    def measure_download_speed(self):
        if self.speed_measurement_thread is not None and self.speed_measurement_thread.isRunning():
            return

        self.label_result.setText("Realizando medición de descarga...")
        self.label_result.setAlignment(Qt.AlignCenter)
        self.button_measure_download.setEnabled(False)
        self.button_measure_upload.setEnabled(False)

        self.speed_measurement_thread = SpeedMeasurementThread(download=True)
        self.speed_measurement_thread.measurement_done.connect(self.display_download_speed)
        self.speed_measurement_thread.start()

    def measure_upload_speed(self):
        if self.speed_measurement_thread is not None and self.speed_measurement_thread.isRunning():
            return

        self.label_result.setText("Realizando medición de subida...")
        self.label_result.setAlignment(Qt.AlignCenter)
        self.button_measure_download.setEnabled(False)
        self.button_measure_upload.setEnabled(False)

        self.speed_measurement_thread = SpeedMeasurementThread(download=False)
        self.speed_measurement_thread.measurement_done.connect(self.display_upload_speed)
        self.speed_measurement_thread.start()

    def display_download_speed(self, speed):
        if speed == -1:
            self.label_result.setText("Error al obtener la configuración del servidor")
        else:
            self.label_result.setText(f"Velocidad de descarga: {speed:.2f} Mbps")

        self.button_measure_download.setEnabled(True)
        self.button_measure_upload.setEnabled(True)

    def display_upload_speed(self, speed):
        if speed == -1:
            self.label_result.setText("Error al obtener la configuración del servidor")
        else:
            self.label_result.setText(f"Velocidad de subida: {speed:.2f} Mbps")

        self.button_measure_download.setEnabled(True)
        self.button_measure_upload.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

