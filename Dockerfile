FROM python:3-alpine

ENV PROJ_DIR="/app"
ENV LOG_FILE="${PROJ_DIR}/app.log"
ENV CRON_SPEC="* * * * *" 

WORKDIR ${PROJ_DIR}

COPY . ${PROJ_DIR}

RUN pip install -r requirements.txt
RUN echo "${CRON_SPEC} python ${PROJ_DIR}/main.py >> ${LOG_FILE} 2>&1" > ${PROJ_DIR}/crontab
RUN touch ${LOG_FILE} # Needed for the tail
RUN crontab ${PROJ_DIR}/crontab
RUN crontab -l
CMD crond  && tail -f ${LOG_FILE} #crond runs per default in the background