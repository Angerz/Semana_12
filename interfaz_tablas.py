import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt

class ImageGallery(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Image Gallery')
        self.setMinimumSize(830, 730)  # Cambiar el tamaño mínimo de la ventana
        self.setStyleSheet('background-color: #D1E9FF;')  # Cambiar el color de fondo
        
        # Lista de nombres de archivo y títulos de las imágenes
        self.image_files = ['Tablas_17-10.png', 'Tablas_17-11.png', 'Tablas_17-12.jpeg', 'Tabla_17-13.png', 'Tabla_17-14.png']
        self.image_titles = ['Tabla 17-10', 'Tabla 17-11', 'Tabla 17-12', 'Tabla 17-13', 'Tabla 17-14']
        self.current_image_index = 0
        
        # Etiqueta para mostrar la imagen y el título
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.title_label = QLabel(self)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet('font-size: 36px; font-weight: bold;')  # Cambiar el tamaño y estilo de fuente del título
        
        # Botones de adelante y atrás
        self.prev_button = QPushButton('<<', self)
        self.next_button = QPushButton('>>', self)
        
        # Establecer el tamaño de los botones
        self.prev_button.setFixedSize(100, 50)
        self.next_button.setFixedSize(100, 50)
        
        # Conectar los botones a las funciones correspondientes
        self.prev_button.clicked.connect(self.show_prev_image)
        self.next_button.clicked.connect(self.show_next_image)
        
        # Diseño de la interfaz con un layout vertical y horizontal
        image_layout = QVBoxLayout()
        image_layout.addWidget(self.image_label)
        image_layout.addWidget(self.title_label)
        
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.prev_button)
        button_layout.addStretch()
        button_layout.addWidget(self.next_button)
        
        main_layout = QVBoxLayout()
        main_layout.addLayout(image_layout)
        main_layout.addLayout(button_layout)
        
        self.setLayout(main_layout)
        
        # Mostrar la primera imagen al iniciar
        self.show_image()
        
    def show_image(self):
        # Cargar la imagen actual y mostrarla en la etiqueta
        image_path = self.image_files[self.current_image_index]
        pixmap = QPixmap(image_path)
        self.image_label.setPixmap(pixmap.scaled(800, 600, Qt.AspectRatioMode.KeepAspectRatio))  # Ajustar el tamaño de la imagen
        self.image_label.setFixedSize(800, 600)  # Cambiar el tamaño fijo de la etiqueta de la imagen
        
        # Mostrar el título de la imagen actual
        title = self.image_titles[self.current_image_index]
        self.title_label.setText(title)
        
    def show_prev_image(self):
        # Cambiar al índice de imagen anterior
        self.current_image_index -= 1
        if self.current_image_index < 0:
            self.current_image_index = len(self.image_files) - 1
        self.show_image()
        
    def show_next_image(self):
        # Cambiar al índice de imagen siguiente
        self.current_image_index += 1
        if self.current_image_index >= len(self.image_files):
            self.current_image_index = 0
        self.show_image()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gallery = ImageGallery()
    gallery.show()
    sys.exit(app.exec_())
