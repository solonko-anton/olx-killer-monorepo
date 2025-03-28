import { useTranslation } from 'react-i18next'

import {
  Avatar,
  AvatarFallback,
  AvatarImage,
} from '@/shared/ui/shadcn-ui/avatar'
import { PhoneIcon } from '@/shared/ui'
import avatar_img from '../assets/photo.jpg'

export const MessageHeader = () => {
  const { t } = useTranslation()

  return (
    <div className='flex items-center justify-between p-6'>
      <div className='flex items-start gap-3'>
        <Avatar className='h-[52px] w-[52px]'>
          <AvatarImage src={avatar_img} />
          <AvatarFallback>CN</AvatarFallback>
        </Avatar>
        <div className='space-y-2'>
          <p className='text-sm/[21px] font-semibold text-gray-950'>John Doe</p>
          <p className='flex items-center gap-1.5 text-xs/[14.52px] text-gray-950'>
            <span className='flex size-[18px] items-center justify-center'>
              <span className='flex size-2 rounded-full bg-green' />
            </span>
            <span>{t('chat.status')}</span>
          </p>
        </div>
      </div>
      <button className='flex size-[52px] items-center justify-center rounded-full border border-border text-primary-900'>
        <PhoneIcon />
      </button>
    </div>
  )
}
