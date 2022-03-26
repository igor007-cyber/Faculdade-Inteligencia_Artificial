#pip install opencv-python < Instalar antes de rodar

# CARREGA DEPENDENCIAS ?
import time
import cv2

# CORES DE CLASSES
COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]

# Carregando as classes
class_name = []
with open('coco.names','r') as f:
    class_names = [cname.strip() for cname in f.readlines()]

# Captura de Video
    #Use 0 para usar webcam ou coloque o caminho de um video entre e sua extensão''
        #Exemplo: cap = cv2.VideoCapture('videoplayback.mp4')
cap = cv2.VideoCapture(0)

# Carregando Peso da Rede NEURAL > tiny = leve
net = cv2.dnn.readNet('yolov4-tiny.weights', 'yolov4-tiny.cfg')

# Parametros da Rede Neural
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(416, 416), scale=1/255)

# Leitura dos frames do video
prev_frame = 0 # Frame anterior, usado para calcular o FPS
start = 0
while True:
    
    # Captura do frame
    _, frame = cap.read()
    
    # Começo da contagem dos MS
    start = time.time()
    
    # Detectação
    classes, scores, boxes = model.detect(frame, 0.1, 0.2)
    
    # Fim da Contagem MS
    end = time.time()
    
    #Pecorrer todas as detectações
    for (classid, score, box) in zip(classes, scores, boxes):
        
        # Gerando cores para as classes
        color = COLORS[int(classid) % len(COLORS)]
        
        # Pegando o nome da classe pelo ID e o seu Score
        label = f'{class_names[classid]} : {int(score*100)}%'
        
        # Desenhando a Box da detectação
        cv2.rectangle(frame, box, color, 1)
        
        # Escrevendo o nome da classe em cima da box do objeto
        cv2.putText(frame, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
        
    # Calculando o tempo que levou para fazer a detecção
        #FPS
    fps_label = 1/(start-prev_frame)
    prev_frame = start
    fps_label = int(fps_label)
    fps_label = str(fps_label)
    
    # Escrevendo o FPS na Imagem
    cv2.putText(frame, fps_label, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0 , 0), 5)
    cv2.putText(frame, fps_label, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255 , 0), 3)
    
    # Criando a janela
    cv2.imshow('detections', frame)
    
    # Apertando Q no teclado a qualquer momento para fechar o programa
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# Liberação da camera e destroi todas as janelas
cap.release()
cv2.destroyAllWindows()
    
    
    
    
    
    
    
    
    
    
    
    
    
